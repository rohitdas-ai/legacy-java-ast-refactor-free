# Legacy Java to Spring Boot Refactoring — Community Edition

> **Free discovery gateway and Java monolith project analyzer.**
> For automated AST domain extraction, dependency resolution, Spring Boot 3.4 scaffolding, and PR creation,
> upgrade to the **Enterprise edition** on [MCPize →](https://mcpize.com/mcp/legacy-java-microservices-refactor-mcp)

---

## What This Does

This free MCP server connects to your local codebase and allows your AI client to:

- ✅ Scan local Java package directories
- ✅ Discover monolithic project structures and classes
- ❌ **Does NOT** run deep AST domain boundary analysis (Enterprise only)
- ❌ **Does NOT** rewrite code or translate annotations (Enterprise only)
- ❌ **Does NOT** scaffold Spring Boot 3.4 microservices (Enterprise only)
- ❌ **Does NOT** validate Maven dependencies or build compilation (Enterprise only)

---

## Install

No external packages are required except the standard MCP SDK.

```bash
pip install mcp
```

## Usage

### Run as stdio MCP server

```bash
python server.py
```

### Configure in your MCP client (e.g., Claude Desktop or Cursor)

Add the following block to your client configurations:

```json
{
  "mcpServers": {
    "legacy-java-refactor-free": {
      "command": "python",
      "args": ["/path/to/freemium-stub/server.py"]
    }
  }
}
```

### Available Tools

#### `refactor_java_monolith`
Prompts the refactoring gateway to begin analysis.

* **Arguments:**
  * `target_path` *(string)*: Absolute path to the source root of the legacy Java package to analyze.

---

## Enterprise Features (Upgrade to Unlock)

| Feature | Community (Free) | Enterprise ($49.99/mo) |
| :--- | :---: | :---: |
| Monolith directory discovery | ✅ | ✅ |
| Identify Java class structures | ✅ | ✅ |
| **Advanced AST Domain Boundary Analysis** | ❌ | **✅ (Included)** |
| **Jakarta EE to Spring Boot 3.4 Scaffolding** | ❌ | **✅ (Included)** |
| **Automated Dependency Mapping & Validation** | ❌ | **✅ (Included)** |
| **Enterprise Sandbox Execution Controls** | ❌ | **✅ (Included)** |

**[→ Upgrade on MCPize](https://mcpize.com/mcp/legacy-java-microservices-refactor-mcp)**

---

## License

MIT — Community Edition only. Enterprise refactoring core-logic is proprietary.
