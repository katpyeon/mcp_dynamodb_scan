# DynamoDB Scanner
[![smithery badge](https://smithery.ai/badge/@katpyeon/mcp_dynamodb_scan)](https://smithery.ai/server/@katpyeon/mcp_dynamodb_scan)

> ## ⚠️ 주요 주의사항
>
> - DynamoDB Scan 작업은 전체 테이블 데이터를 탐색하므로 상당한 비용이 발생함
> - 결과 최대 크기가 1MB로 제한되어 있어 필요한 모든 데이터를 얻기 위해서는 페이지네이션으로 추가 검색 필요
> - 이 도구는 테스트 용도로만 사용 권장
> - 프로덕션 환경에서는 본인의 데이터 접근 패턴에 맞게 Query 기능으로 재구현하는 것이 효율적
> - 대규모 데이터 스캔 시 DynamoDB 처리량(RCU) 소비에 주의

DynamoDB Scanner는 AWS DynamoDB 테이블을 스캔하고 필터링할 수 있는 간편한 도구입니다. [FastMCP](https://github.com/michaelcurtis/fastmcp) 프레임워크를 기반으로 하며, AWS 콘솔과 유사한 방식으로 DynamoDB 테이블의 데이터를 탐색하고 필터링할 수 있습니다.

## 주요 기능

- DynamoDB 테이블 스캔 (전체 또는 필터링)
- 테이블 스키마 정보 확인
- 페이지네이션 지원
- AWS 콘솔과 유사한 사용자 경험

## 설치 및 설정

### Installing via Smithery

To install DynamoDB Scanner for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@katpyeon/mcp_dynamodb_scan):

```bash
npx -y @smithery/cli install @katpyeon/mcp_dynamodb_scan --client claude
```

### 1. 저장소 복제

```bash
git clone https://github.com/yourusername/mcp_dynamodb_scan.git
cd mcp_dynamodb_scan
```

### 2. 가상환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 의존성 패키지 설치
pip install -r requirements.txt
```

### 3. Claude 설정

이 프로젝트는 Claude와 함께 사용하도록 설계되었습니다. Claude Developer Console에서 다음과 같이 프로필을 설정하세요:

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

위 설정에서 환경변수 항목에 적절한 값을 채워넣으세요:

- `DYNAMO_TABLE_NAME`: 스캔할 DynamoDB 테이블 이름
- `AWS_ACCESS_KEY_ID`: AWS 접근 키 ID
- `AWS_SECRET_ACCESS_KEY`: AWS 보안 액세스 키
- `AWS_REGION`: AWS 리전 (예: ap-northeast-2)

## 사용법

애플리케이션을 실행하려면:

```bash
python app.py
```

이제 FastMCP 서버가 시작되며, Claude와 통합하여 DynamoDB 테이블을 스캔하고 필터링할 수 있습니다.

### 예제 쿼리

Claude에게 다음과 같은 요청을 할 수 있습니다:

1. "테이블 스키마를 보여줘"
2. "이름이 '홍길동'인 항목 찾아줘"
3. "모든 사용자 정보를 보여줘"

## 라이센스

이 프로젝트는 MIT 라이센스 하에 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
