[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/katpyeon-mcp-dynamodb-scan-badge.png)](https://mseep.ai/app/katpyeon-mcp-dynamodb-scan)

# DynamoDB Scanner

[![smithery badge](https://smithery.ai/badge/@katpyeon/mcp_dynamodb_scan)](https://smithery.ai/server/@katpyeon/mcp_dynamodb_scan)

> ## ⚠️ Important Notice
>
> - DynamoDB Scan operation scans the entire table, which can incur significant costs.
> - The maximum result size is limited to 1MB, so you may need to use pagination to retrieve all desired data.
> - This tool is recommended for testing purposes only.
> - For production, it is more efficient to implement Query operations tailored to your data access patterns.
> - Be aware of DynamoDB read capacity (RCU) consumption when scanning large datasets.

DynamoDB Scanner is a simple tool for scanning and filtering AWS DynamoDB tables. It is based on the [FastMCP](https://github.com/michaelcurtis/fastmcp) framework and provides an experience similar to the AWS Console for exploring and filtering DynamoDB table data.

## Features

- Scan DynamoDB tables (full or filtered)
- View table schema information
- Pagination support
- User experience similar to AWS Console

## Installation & Setup

### Installing via Smithery

To install DynamoDB Scanner for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@katpyeon/mcp_dynamodb_scan):

```bash
npx -y @smithery/cli install @katpyeon/mcp_dynamodb_scan --client claude
```

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mcp_dynamodb_scan.git
cd mcp_dynamodb_scan
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Claude Profile Configuration

This project is designed to work with Claude. Set up your profile in the Claude Developer Console as follows:

```json
"dynamodb-scanner": {
  "command": "/Users/yourname/path/mcp_dynamodb_scan/.venv/bin/python",
  "args": ["/Users/yourname/path/mcp_dynamodb_scan/app.py"],
  "env": {
    "DYNAMO_TABLE_NAME": "",
    "AWS_ACCESS_KEY_ID": "",
    "AWS_SECRET_ACCESS_KEY": "",
    "AWS_REGION": ""
  },
  "port": 8080
}
```

Fill in the environment variables with appropriate values:

- `DYNAMO_TABLE_NAME`: Name of the DynamoDB table to scan
- `AWS_ACCESS_KEY_ID`: AWS Access Key ID
- `AWS_SECRET_ACCESS_KEY`: AWS Secret Access Key
- `AWS_REGION`: AWS Region (e.g., ap-northeast-2)

## Usage

To run the application:

```bash
python app.py
```

The FastMCP server will start, and you can use it with Claude to scan and filter DynamoDB tables.

### Example Queries

You can ask Claude:

1. "Show me the table schema."
2. "Find items where the name is 'Hong Gil-dong'."
3. "Show me all user information."

## License

This project is distributed under the MIT License. See the LICENSE file for details.


---

<a href="https://www.buymeacoffee.com/katpyeon" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="40" />
</a>