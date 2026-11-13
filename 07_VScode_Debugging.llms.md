# Vscode Debugging

Vscode debugging

Author

Benedict Thekkel

## Install debugpy

    poetry add debugpy

------------------------------------------------------------------------

## VScode launch.json file

> The `launch.json` file in Visual Studio Code (VS Code) is part of its debugging configuration. It allows you to define how your project or application should be launched and debugged. Below is everything you need to know about the `launch.json` file, including its structure, key fields, and advanced configurations.

------------------------------------------------------------------------

### **What is `launch.json`?**

- A configuration file used by VS Code to define debugging settings.
- It resides in the `.vscode` folder in your project directory.
- It supports multiple configurations for debugging different scenarios (e.g., running a script, attaching to a remote debugger, or debugging tests).

------------------------------------------------------------------------

### **Location of `launch.json`**

- Located in `.vscode/launch.json` in your project directory.
- If it doesn’t exist, VS Code will prompt you to create one when you click the “Run and Debug” sidebar and select “Create a launch.json file.”

------------------------------------------------------------------------

### **Structure of `launch.json`**

A `launch.json` file consists of an array of configurations:

``` json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Script",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/script.py",
            "console": "integratedTerminal"
        }
    ]
}
```

- **`version`**: Specifies the version of the debugging schema. Use `0.2.0`.
- **`configurations`**: An array of objects, each defining a specific debugging scenario.

------------------------------------------------------------------------

### **Key Fields in `launch.json`**

#### **General Fields**

- **`name`**: The display name of the configuration in the Run and Debug dropdown.
- **`type`**: The debugger type (e.g., `python`, `node`, `java`, etc.).
- **`request`**:
  - `launch`: Starts the program or application.
  - `attach`: Attaches to a running process for debugging.
- **`program`**: The entry point of your application (e.g., a script path).
- **`args`**: Arguments to pass to the program.
- **`console`**:
  - `integratedTerminal`: Use VS Code’s built-in terminal.
  - `externalTerminal`: Use an external terminal.

#### **Python-Specific Fields**

- **`pythonPath`**: Path to the Python interpreter. If omitted, VS Code uses the Python interpreter set in the workspace.
- **`django`**: Set to `true` to enable Django debugging.
- **`justMyCode`**: Set to `false` to step into library code during debugging.

#### **Remote Debugging**

- **`host`**: The remote machine’s hostname or IP address.
- **`port`**: The port to connect to (e.g., for `debugpy`).
- **`pathMappings`**: Maps local and remote file paths for remote debugging.

#### **Environment Variables**

- **`env`**: Defines environment variables for the debug session.
- **`envFile`**: Path to a `.env` file containing environment variables.

#### **Advanced Debugging**

- **`stopOnEntry`**: Stops execution at the entry point of the program.
- **`logToFile`**: Saves debugger logs to a file.
- **`cwd`**: Sets the working directory of the application.

### **Common Configurations**

#### 1. **Run a Python Script**

``` json
{
    "name": "Run Script",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/script.py",
    "console": "integratedTerminal"
}
```

#### 2. **Debug Django**

``` json
{
    "name": "Django Debug",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/manage.py",
    "args": ["runserver", "--noreload"],
    "django": true,
    "env": {
        "DEBUG": "1"
    },
    "console": "integratedTerminal"
}
```

#### 3. **Attach to Debugpy**

``` json
{
    "name": "Attach to Debugpy",
    "type": "python",
    "request": "attach",
    "host": "localhost",
    "port": 5678,
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "${workspaceFolder}"
        }
    ]
}
```

#### 4. **Run Tests**

``` json
{
    "name": "Run Tests",
    "type": "python",
    "request": "test",
    "console": "integratedTerminal",
    "justMyCode": true
}
```

#### 5. **Debug Flask**

``` json
{
    "name": "Flask Debug",
    "type": "python",
    "request": "launch",
    "module": "flask",
    "env": {
        "FLASK_APP": "app.py",
        "FLASK_ENV": "development"
    },
    "args": ["run"],
    "console": "integratedTerminal"
}
```

#### 6. **Node.js Application**

``` json
{
    "name": "Node.js Debug",
    "type": "node",
    "request": "launch",
    "program": "${workspaceFolder}/app.js"
}
```

### **Path Variables in `launch.json`**

- **`${workspaceFolder}`**: Path to the root folder of your workspace.
- **`${file}`**: Path to the currently open file.
- **`${relativeFile}`**: Relative path of the open file.
- **`${cwd}`**: Current working directory.

------------------------------------------------------------------------

### **Environment Variables in `launch.json`**

#### Inline Environment Variables

``` json
"env": {
    "DEBUG": "true",
    "API_KEY": "12345"
}
```

#### Use an `.env` File

``` json
"envFile": "${workspaceFolder}/.env"
```

`.env` file example:

    DEBUG=true
    API_KEY=12345

------------------------------------------------------------------------

### **Debugging Scenarios**

#### **Remote Debugging**

To debug a process running on a remote server: 1. Run `debugpy` or equivalent on the server, exposing a port (e.g., `5678`). 2. Use an `attach` configuration in `launch.json` with the server’s IP and port.

#### **Debugging Docker**

1.  Expose the debug port in your Docker container.
2.  Map local paths to container paths using `pathMappings`.

#### **Conditional Debugging**

Use conditions to enable debugging only for specific scenarios:

``` json
"condition": "process.env.DEBUG === 'true'"
```

------------------------------------------------------------------------

### **Common Issues and Solutions**

1.  **Breakpoints Not Hit**
    - Ensure the debugger is attached correctly.
    - Verify file paths in `pathMappings`.
2.  **Port Conflicts**
    - Change the debug port if another process uses it.
3.  **Debugger Not Attaching**
    - Ensure the `debugpy` or equivalent is listening on the expected port.
    - Check firewall settings for remote debugging.
4.  **Library Code Not Stepped Into**
    - Set `"justMyCode": false` to debug library code.

------------------------------------------------------------------------

### **Best Practices**

1.  **Use Descriptive Names** Use meaningful names for configurations to identify them quickly.

2.  **Organize Configurations** Group related configurations together, such as separate entries for running tests, debugging the server, or attaching to remote processes.

3.  **Environment-Specific Settings** Use different configurations for development, staging, and production environments.

Back to top
