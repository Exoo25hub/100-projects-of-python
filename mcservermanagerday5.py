import os
import subprocess
import time
import signal

# Change this to your Minecraft server JAR file
MINECRAFT_JAR = "server.jar"
MINECRAFT_DIR = "/path/to/your/server"  # Change this to your server directory

server_process = None  # Holds the running process


def start_server():
    """Starts the Minecraft server."""
    global server_process
    if server_process:
        print("Server is already running!")
        return

    os.chdir(MINECRAFT_DIR)
    print("Starting Minecraft server...")

    server_process = subprocess.Popen(
        ["java", "-Xmx2G", "-Xms1G", "-jar", MINECRAFT_JAR, "nogui"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("Minecraft server started!")


def stop_server():
    """Stops the Minecraft server."""
    global server_process
    if not server_process:
        print("Server is not running!")
        return

    print("Stopping server...")
    server_process.send_signal(signal.SIGTERM)
    server_process = None
    print("Minecraft server stopped.")


def check_status():
    """Checks if the Minecraft server is running."""
    if server_process and server_process.poll() is None:
        print("Minecraft server is running.")
    else:
        print("Minecraft server is NOT running.")


def restart_server():
    """Restarts the Minecraft server."""
    stop_server()
    time.sleep(5)  # Wait before restarting
    start_server()


def main():
    """Simple CLI for managing the Minecraft server."""
    while True:
        print("\n--- Minecraft Server Manager ---")
        print("1. Start Server")
        print("2. Stop Server")
        print("3. Check Server Status")
        print("4. Restart Server")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            start_server()
        elif choice == "2":
            stop_server()
        elif choice == "3":
            check_status()
        elif choice == "4":
            restart_server()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
