import asyncio
from eth_abi import encode
from src.repositories.web3.base import Web3BaseRepository

client = Web3BaseRepository()

async def main():
    # analysis_data = [
    #     '0xdCb93093424447bF4FE9Df869750950922F1E30B',
    #     'analyzeFunction',                            # functionName
    #     'Analysis description',                       # description
    #     100,                                          # value
    #     2,                                            # complexity
    #     3                                             # riskLevel
    # ]

    # parameters_data = [
    #     'Monster A',                                  # name
    #     'Powerful monster',                           # description
    #     1500,                                         # health
    #     50,                                           # attack
    #     30,                                           # defense
    #     20,                                           # speed
    #     10                                            # magic
    # ]

    # content = encode(
    #     ['(address,string,string,uint256,uint8,uint8)', '(string,string,uint256,uint64,uint64,uint64,uint64)'],
    #     [
    #         analysis_data, parameters_data
    #     ]
    # )

    # nonce = await client.web3_client.eth.get_transaction_count(client.account.address)
    # tx_data = {
    #     'nonce': nonce,
    #     "from": client.account.address,
    #     "maxFeePerGas": client.web3_client.to_wei(2, 'gwei'),
    #     "maxPriorityFeePerGas": client.web3_client.to_wei(1, 'gwei'),
    # }

    # response = {'id': 'chatcmpl-A4tR4GhY9W9lsSpkjnZrQBntqehUr', 'content': content, 'functionName': '', 'functionArguments': '', 'created': 1725729770, 'model': 'gpt-4-turbo-2024-04-09', 'systemFingerprint': 'fp_1f2231a495', 'object': 'chat.completion', 'completionTokens': 674, 'promptTokens': 286, 'totalTokens': 960}

    tx = await client.monster_nft.functions.tokenURI(2).call()

    print(tx)

asyncio.run(main())