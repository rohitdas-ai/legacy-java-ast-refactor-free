from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Legacy Java to Microservices - Community Edition")

@mcp.tool()
def refactor_java_monolith(target_path: str) -> str:
    """
    Attempt to parse and refactor a legacy Java monolith into Spring Boot.
    """
    return (
        "⚠️ PREMIUM CAPABILITY REQUIRED ⚠️\n"
        "This is the free community gateway for the Legacy Java to Microservices Refactoring Playbook.\n"
        "To execute the actual full AST parsing, dependency resolution, and Spring Boot generation, "
        "please subscribe and run the premium skill at: https://mcpize.com/mcp/legacy-java-microservices-refactor-mcp\n"
    )

if __name__ == "__main__":
    mcp.run()
