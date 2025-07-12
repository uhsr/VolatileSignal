# VolatileSignal: Decentralized Crypto Price Alerts

Real-time crypto price alerts powered by on-chain oracles and serverless functions, triggered by smart contract events.

VolatileSignal is a revolutionary system designed to provide users with immediate notifications about significant price fluctuations in the cryptocurrency market. Unlike traditional centralized alert services, VolatileSignal leverages the power of decentralized on-chain oracles and serverless functions to ensure reliability, transparency, and security. By monitoring smart contract events emitted by these oracles, the system can detect price changes with minimal latency and relay this information to users through WebSockets. This allows users to react quickly to market movements, enabling them to make informed trading decisions and manage their portfolios effectively.

The core innovation lies in its decentralized architecture. By relying on established on-chain oracles (e.g., Chainlink, Band Protocol) for price data, VolatileSignal eliminates the single point of failure associated with centralized data feeds. The use of serverless functions (e.g., AWS Lambda, Google Cloud Functions) further enhances scalability and reduces operational overhead. These functions are triggered by events emitted by the oracle smart contracts, processing the price data and sending alerts to subscribed users via WebSockets. This event-driven approach ensures that alerts are delivered in near real-time, maximizing their utility for traders and investors.

VolatileSignal offers a robust and customizable solution for anyone seeking to stay ahead of the volatile cryptocurrency market. Its decentralized nature ensures data integrity and reliability, while its serverless architecture provides scalability and cost-efficiency. The use of WebSockets enables instant alert delivery, allowing users to react swiftly to market changes. Whether you are a seasoned trader or a casual investor, VolatileSignal empowers you to monitor your assets effectively and capitalize on opportunities in the dynamic world of cryptocurrency.

Key Features:

*   **Decentralized Price Data:** Employs on-chain oracles like Chainlink or Band Protocol to fetch price data, ensuring data integrity and eliminating single points of failure. Specifically, it monitors the `AnswerUpdated` event emitted by Chainlink price feed contracts.
*   **Real-time Alerts:** Leverages WebSockets for instant delivery of price alerts to subscribed users. The serverless function establishes a persistent connection with a WebSocket gateway (e.g., AWS API Gateway) for efficient message delivery.
*   **Serverless Architecture:** Utilizes serverless functions (e.g., AWS Lambda) to process price data and trigger alerts, ensuring scalability and cost-effectiveness. The serverless functions are triggered by events emitted by the oracle smart contracts.
*   **Smart Contract Event Monitoring:** Listens to smart contract events emitted by the on-chain oracles to detect price changes. Uses a provider library like Web3.py to interact with the Ethereum blockchain.
*   **Customizable Alert Thresholds:** Allows users to define custom price thresholds for triggering alerts. Users can specify percentage changes or absolute price levels that will trigger a notification.
*   **WebSocket Authentication:** Implements robust authentication mechanisms for WebSocket connections to ensure only authorized users receive alerts. This can include JWT-based authentication or API keys.
*   **Scalable Infrastructure:** Designed to handle a large number of users and price feeds with minimal latency. The serverless architecture allows for automatic scaling based on demand.

Technology Stack:

*   **Python:** The primary programming language used for developing the serverless functions and WebSocket server logic.
*   **Web3.py:** A Python library for interacting with the Ethereum blockchain and smart contracts. Used to monitor oracle smart contract events.
*   **WebSockets:** A communication protocol that provides full-duplex communication channels over a single TCP connection. Used for real-time alert delivery.
*   **AWS Lambda (or Google Cloud Functions):** A serverless compute service used to run the price processing logic and trigger alerts.
*   **Chainlink (or Band Protocol):** A decentralized oracle network providing reliable price data.
*   **Redis (optional):** Used for caching price data and managing WebSocket connections.

Installation:

1.  Clone the repository:
    git clone https://github.com/uhsr/VolatileSignal.git
    cd VolatileSignal

2.  Install Python dependencies:
    pip install -r requirements.txt

3.  Install Node.js and npm: (Required for deploying WebSocket gateway if using AWS API Gateway)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    nvm install node

4.  Deploy the WebSocket gateway (if using AWS API Gateway): Follow AWS documentation for setting up a WebSocket API Gateway. You may need to deploy a separate handler function for connection, disconnection and message handling.

Configuration:

1.  Set up environment variables: Create a `.env` file in the root directory and add the following variables:

    *   `WEB3_PROVIDER_URL`: The URL of your Ethereum node provider (e.g., Infura, Alchemy).
    *   `CHAINLINK_ETH_USD_ADDRESS`: The address of the Chainlink ETH/USD price feed contract.
    *   `WEBSOCKET_API_ENDPOINT`: The endpoint of your WebSocket API Gateway.
    *   `ALERT_THRESHOLD`: The default percentage change threshold for triggering alerts.
    *   `REDIS_HOST` (optional): The host of your Redis server.
    *   `REDIS_PORT` (optional): The port of your Redis server.

2.  Configure the `config.py` file: Update the `config.py` file with any custom settings.

Usage:

1.  Run the serverless function: Deploy the `handler.py` function to your serverless provider (e.g., AWS Lambda). Ensure that the function has the necessary permissions to access the Ethereum node and send messages to the WebSocket gateway.

2.  Connect to the WebSocket API: Use a WebSocket client to connect to the `WEBSOCKET_API_ENDPOINT`. You can send JSON messages to subscribe to specific price feeds and alert thresholds.

    Example client connection (python):
    import asyncio
    import websockets
    async def connect():
        uri = "wss://your-websocket-api-endpoint"
        async with websockets.connect(uri) as websocket:
            await websocket.send('{"subscribe": {"asset": "ETH/USD", "threshold": 5}}')
            while True:
                message = await websocket.recv()
                print(f"< {message}")
    asyncio.run(connect())

Contributing:

We welcome contributions to VolatileSignal! Please follow these guidelines:

*   Fork the repository and create a new branch for your feature or bug fix.
*   Write clear and concise commit messages.
*   Submit a pull request with a detailed description of your changes.
*   Ensure that your code adheres to the project's coding standards.
*   Include unit tests for any new functionality.

License:

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/VolatileSignal/blob/main/LICENSE) file for details.

Acknowledgements:

We would like to acknowledge the following projects and communities for their contributions to the development of VolatileSignal:

*   Chainlink and Band Protocol for providing reliable on-chain oracle data.
*   The Web3.py community for creating a powerful tool for interacting with the Ethereum blockchain.
*   The Serverless framework community for providing a platform for building and deploying serverless applications.