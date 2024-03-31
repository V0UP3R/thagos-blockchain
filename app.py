from flask import Flask, jsonify, request
from blockchain import Blockchain
from uuid import uuid4

app = Flask(__name__)
blockchain = Blockchain()

node_identifier = str(uuid4()).replace('-', '')

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New block forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    user_address = request.args.get('user_address')
    balance = blockchain.get_balance(user_address)
    response = {'balance': balance}
    return jsonify(response), 200

@app.route('/wallet/new', methods=['GET'])
def generate_wallet():
    wallet_address = blockchain.generate_wallet()
    response = {'wallet_address': wallet_address}
    return jsonify(response), 200

@app.route('/transaction/sign', methods=['POST'])
def sign_transaction():
    values = request.get_json()

    required = ['sender_wallet_address', 'transaction_data']
    if not all(k in values for k in required):
        return 'Missing values', 400

    signature = blockchain.sign_transaction(values['sender_wallet_address'], values['transaction_data'])

    response = {'signature': signature.hex()}
    return jsonify(response), 200

@app.route('/transactions/submit', methods=['POST'])
def submit_transaction():
    values = request.get_json()

    required = ['sender_wallet_address', 'recipient', 'amount', 'signature']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockchain.new_transaction(values['sender_wallet_address'], values['recipient'], values['amount'], values['signature'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200

@app.route('/block/<int:block_index>', methods=['GET'])
def get_block(block_index):
    block = blockchain.get_block_by_index(block_index)
    if block:
        return jsonify(block), 200
    else:
        return 'Block not found', 404
    
@app.route('/network/status', methods=['GET'])
def network_status():
    response = {
        'total_nodes': len(blockchain.nodes),
        'nodes': list(blockchain.nodes)
    }
    return jsonify(response), 200

@app.route('/node/<node_url>', methods=['GET'])
def get_node(node_url):
    if node_url in blockchain.nodes:
        response = {
            'node_url': node_url,
            'status': 'online' 
        }
        return jsonify(response), 200
    else:
        return 'Node not found', 404
    
@app.route('/blockchain/stats', methods=['GET'])
def blockchain_stats():
    response = {
        'total_blocks': len(blockchain.chain),
        'total_transactions': sum(len(block['transactions']) for block in blockchain.chain),
    }
    return jsonify(response), 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
