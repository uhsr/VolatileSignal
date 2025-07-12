# VolatileSignal: Ephemeral Data Propagation

VolatileSignal is a Python library designed to facilitate the propagation of ephemeral data signals between decoupled components or processes. It addresses the challenge of transient data transfer where persistence is unnecessary, and immediate propagation is paramount. This library leverages a combination of in-memory storage and asynchronous event handling to ensure timely delivery of signals while minimizing overhead. Unlike traditional message queues, VolatileSignal prioritizes speed and simplicity for data that is inherently short-lived and contextually relevant only within a defined timeframe.

The core concept behind VolatileSignal is the "Signal" object, which acts as a container for the transient data. These signals are published to specific "Channels," which serve as logical grouping mechanisms for related signals. Subscribers to a channel receive all signals published on that channel as soon as they are available. The library utilizes asynchronous programming with `asyncio` to provide non-blocking signal delivery, enabling high concurrency and responsiveness. A built-in expiration mechanism automatically removes signals from the channel after a configurable timeout, preventing memory leaks and ensuring that only relevant data is processed. The library offers a robust error-handling strategy, allowing developers to define custom error callbacks for signal delivery failures.

VolatileSignal is particularly well-suited for applications involving real-time data processing, inter-process communication within a single machine, and event-driven architectures where data volatility is a key characteristic. For example, it can be used to propagate sensor readings, system status updates, or user interface events between different modules of an application. By providing a lightweight and efficient mechanism for ephemeral data propagation, VolatileSignal simplifies the development of complex, reactive systems. It encourages a modular design, allowing components to communicate without direct dependencies, fostering code reusability and maintainability.

Key Features:

*   **Asynchronous Signal Delivery:** Utilizes `asyncio` for non-blocking signal propagation, ensuring high concurrency and responsiveness. Signals are delivered to subscribers asynchronously, preventing bottlenecks in the main event loop.
*   **Channel-Based Propagation:** Employs channels as logical grouping mechanisms for signals, enabling selective signal reception by subscribers. Each signal is published to a specific channel, allowing subscribers to filter signals based on their relevance.
*   **Signal Expiration:** Offers a configurable expiration mechanism to automatically remove signals after a specified timeout. This prevents memory leaks and ensures that only relevant data is processed. The expiration time is configurable per channel.
*   **Error Handling:** Provides a mechanism for defining custom error callbacks for signal delivery failures. This enables developers to handle errors gracefully and implement appropriate recovery strategies. Each channel can have its own error callback.
*   **Thread Safety:** Implements internal locking mechanisms to ensure thread safety, allowing VolatileSignal to be used in multi-threaded applications without data corruption.
*   **Lightweight Footprint:** Designed with a minimal memory footprint and low overhead, making it suitable for resource-constrained environments.
*   **Type Hinting & Documentation:** Full utilization of type hints and comprehensive documentation to facilitate code understanding and usage.

Technology Stack:

*   **Python 3.7+:** The core programming language used for developing VolatileSignal. Its clear syntax and extensive libraries make it ideal for this project.
*   **asyncio:** Python's built-in asynchronous I/O framework. It provides the foundation for non-blocking signal delivery and concurrent event handling.
*   **typing:** Python's type hinting module. It enhances code readability and maintainability by providing static type checking.
*   **concurrent.futures:** Used for executing tasks in separate threads or processes to handle potentially blocking operations asynchronously.

Installation:

1.  Ensure you have Python 3.7 or later installed on your system.
2.  Clone the VolatileSignal repository from GitHub:
    git clone https://github.com/uhsr/VolatileSignal.git
3.  Navigate to the repository directory:
    cd VolatileSignal
4.  Create a virtual environment (optional but recommended):
    python3 -m venv venv
5.  Activate the virtual environment:
    source venv/bin/activate  (on Linux/macOS)
    venv\Scripts\activate  (on Windows)
6.  Install the required dependencies:
    pip install .

Configuration:

VolatileSignal does not rely on external configuration files or environment variables. Channel configurations, such as expiration times and error callbacks, are defined programmatically when creating or accessing channels. This allows for dynamic and context-aware configuration.

Usage:

Import required classes.
from VolatileSignal import Channel, Signal

Create a channel:
channel = Channel("my_channel")

Publish a signal:
async def publish_signal():
    await channel.publish(Signal({"data": "my_data"}))

Subscribe to a channel:
async def subscribe_channel():
    async for signal in channel.subscribe():
        print(signal.data)

Run the publisher and subscriber concurrently:
import asyncio
asyncio.run(asyncio.gather(publish_signal(), subscribe_channel()))

Error callback example:
def error_callback(e):
    print(f"Error: {e}")
channel = Channel("error_channel", error_callback=error_callback)

API Documentation:

*   `Channel(name: str, expiration_time: float = 60.0, error_callback: Callable[[Exception], None] = None)`: Creates a new channel with the specified name, expiration time (in seconds), and error callback.
*   `Channel.publish(signal: Signal)`: Publishes a signal to the channel.
*   `Channel.subscribe()`: Returns an asynchronous iterator that yields signals published to the channel.
*   `Signal(data: Any)`: Creates a new signal with the specified data.

Contributing:

We welcome contributions to VolatileSignal! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with comprehensive tests.
4.  Submit a pull request with a detailed description of your changes.

License:

This project is licensed under the MIT License. See the [LICENSE](https://github.com/uhsr/VolatileSignal/blob/main/LICENSE) file for details.

Acknowledgements:

We would like to acknowledge the developers of `asyncio` for providing the foundation for asynchronous programming in Python. Their work has been instrumental in the development of VolatileSignal.