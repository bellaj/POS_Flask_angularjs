#!/usr/bin/env python
from flask import Flask, jsonify, send_from_directory, request
app = Flask(__name__)
from web3 import Web3
import json
from web3.providers.rpc import HTTPProvider
import rlp
from ethereum.transactions import Transaction

@app.route('/api/v1/get_names')
def get_names():
    names = {'names':
             [
                 'fred',
                 'john',
                 'paul',
                 'greg'
             ]}
    return jsonify(names)

@app.route('/api/v1/get_people')
def get_people():
    people = {"people": [
        {'name': 'fred', 'age': 10},
        {'name': 'john', 'age': 20},
        {'name': 'paul', 'age': 30},
        {'name': 'greg', 'age': 40},
    ]}
    return jsonify(people)


@app.route('/api/v1/get_time')
def get_time():
    import time
    return jsonify({'time': time.time()})

@app.route('/files/style.css', methods=['GET', 'POST'])
def test():
	return send_from_directory("files", "style.css")
	#return render_template('./files/style.css')

@app.route('/files/app.js', methods=['GET', 'POST'])
def test2():
	return send_from_directory("files", "app.js")
	#return render_template('./files/style.css')

@app.route('/')
def index():
    return send_from_directory(".", "index.html")
	
@app.route('/customers', methods=['GET', 'POST'])
def customers():
	total = request.args.get('total')
	return jsonify({'total': total})
	#return send_from_directory("templates","customers.html")

@app.route('/web3/web3.js', methods=['GET', 'POST'])
def web3():
	return send_from_directory("web3", "web3.js")
	
@app.route('/send', methods=['GET', 'POST'])
def send():

	contractAddress = '0xd5855dcce8933cea211fed171a31f19703a3f8be'
	web3 = Web3(HTTPProvider('https://ropsten.infura.io/v2QCDR7v7cgH6fy0y171'))
	abi= json.loads('[{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')
	print(abi)
	fContract = web3.eth.contract(abi,contractAddress)
	print('call const',fContract.call({'from': '0xFed55B453dBb0589ec5433a9318C09f1766D7dAb'}).balanceOf('0xFed55B453dBb0589ec5433a9318C09f1766D7dAb'))
	call_data = fContract.encodeABI('transfer',["0xa5Acc472597C1e1651270da9081Cc5a0b38258E3", 3333])
	print('data',call_data)
	tx = Transaction(
            nonce=web3.eth.getTransactionCount('0xFed55B453dBb0589ec5433a9318C09f1766D7dAb'),
            gasprice=21000,
            startgas=100000,
            to='0xa5Acc472597C1e1651270da9081Cc5a0b38258E3',
            value=12345,
            data=call_data,
	)
	tx.sign('d2432061d3a6cab6a2f3f635c5dda4bb5c0b9c64285c2aa11d586402f66f0507')
	raw_tx = rlp.encode(tx)
	raw_tx_hex = web3.toHex(raw_tx)
	print(raw_tx_hex)
	hash=web3.eth.sendRawTransaction(raw_tx_hex)
	print(hash)
#	return jsonify({'receipts': hash})
	return jsonify({'receipt': hash})


if __name__ == '__main__':
    app.debug = True
    app.run(port=1234)



