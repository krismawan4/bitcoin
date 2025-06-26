# Bitcoin Cryptography Implementation

Simple Bitcoin cryptography implementation that generates BTC addresses from scratch and sends custom transactions with Bitcoin Core RPC.

**🎥 Featured in my YouTube video:** https://youtu.be/z2Ju7pcE6wo

## Features

- **Address Generation** (`main.ipynb`): Generate Bitcoin addresses from private keys using secp256k1

  - Legacy addresses (P2PKH)
  - SegWit addresses (Bech32)
  - Private key formats: decimal, hex, WIF
- **Transaction Sending** (`send.ipynb`): Send Bitcoin with custom messages via Bitcoin Core RPC

  - OP_RETURN data embedding
  - PSBT workflow

## Quick Start

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. For transaction sending, create `.env` file:

   ```env
   RPC_USER=your_username
   RPC_PASSWORD=your_password
   RPC_HOST=127.0.0.1
   RPC_PORT=8332
   ```
3. Run the notebooks:

   - `main.ipynb` - Generate Bitcoin addresses
   - `send.ipynb` - Send transactions (requires Bitcoin Core)

## Importing Addresses to Bitcoin Core

After generating addresses, you can import them to Bitcoin Core to monitor transactions:

1. **Get descriptor info** - Open Bitcoin Core console and run:
   ```
   getdescriptorinfo "combo(WIF)"
   ```
   Example:
   ```
   getdescriptorinfo "combo(Kz6dh8Ny4HuCDrWEsyBZsUUjz16ab1hmgR5ihvKFx7wGGFibe7Cc)"
   ```
   
   Response:
   ```json
   {
     "descriptor": "combo(02ffd6ef90a5bb4ca138aaad516560aa80157ae0629a27099660dfd5039bc3fa2b)#l3la8e8y",
     "checksum": "04fk0myz",
     "isrange": false,
     "issolvable": true,
     "hasprivatekeys": true
   }
   ```

2. **Import the descriptor** - Use the descriptor with checksum:
   ```
   importdescriptors '[{"desc": "combo(WIF)#DESCRIPTOR", "timestamp": "now"}]'
   ```
   Example:
   ```
   importdescriptors '[{"desc": "combo(02ffd6ef90a5bb4ca138aaad516560aa80157ae0629a27099660dfd5039bc3fa2b)#l3la8e8y", "timestamp": "now"}]'
   ```

**Note:** The `timestamp` parameter determines when to start scanning for transactions:
- `"now"` - Only scan for new transactions from current time
- `0` - Scan from the beginning of the blockchain (full rescan)
- Unix timestamp - Scan from a specific date (e.g., `1640995200` for Jan 1, 2022)

The descriptor format includes the checksum after the `#` symbol for verification.

## Dependencies

- `ecdsa` - Elliptic curve cryptography
- `base58` - Address encoding
- `bech32` - SegWit address encoding
- `bitcoinrpc` - Bitcoin Core RPC client

## Warning

⚠️ **Educational purposes only.** Do not use for real funds.
