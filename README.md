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

## Dependencies

- `ecdsa` - Elliptic curve cryptography
- `base58` - Address encoding
- `bech32` - SegWit address encoding
- `bitcoinrpc` - Bitcoin Core RPC client

## Warning

⚠️ **Educational purposes only.** Do not use for real funds.
