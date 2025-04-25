from fastmcp import FastMCP
import boto3
from boto3.dynamodb.conditions import Attr
from typing import Optional, Dict
import os

# MCP 서버 인스턴스 생성
mcp = FastMCP(
    name="DynamoDB Scanner",
    description=(
        "This MCP server allows scanning a fixed DynamoDB table. "
        "It supports filtering and pagination, but only supports scan operations.\n"
        "The table name, AWS access key, and secret key must be provided at runtime via environment variables:\n"
        "- DYNAMO_TABLE_NAME\n"
        "- AWS_ACCESS_KEY_ID\n"
        "- AWS_SECRET_ACCESS_KEY\n"
        "- AWS_REGION (default: ap-northeast-2)"
    )
)

# 환경 변수에서 구성 정보 로드
table_name = os.environ["DYNAMO_TABLE_NAME"]
region_name = os.environ.get("AWS_REGION", "ap-northeast-2")

# boto3 세션 및 테이블 객체 생성
session = boto3.Session()
dynamodb = session.resource("dynamodb", region_name=region_name)
table = dynamodb.Table(table_name)

@mcp.tool()
def describe_table_schema() -> dict:
    """
    Return the list of available columns in the DynamoDB table with descriptions.
    Useful for building filter conditions or understanding the data structure.
    """    
    return {
        "columns": {
            "PK": "기본 파티션 키 (Primary Key)",
            "SK": "정렬 키 (Sort Key)",
            "accountChannelCode": "가입 채널 코드",
            "accountLoginId": "계정 로그인 ID",
            "accountLoginPassword": "계정 로그인 비밀번호",
            "accountNewsSubscription": "뉴스레터 수신 동의 여부",
            "accountRegistrationSource": "회원가입 출처",
            "accountRegistrationType": "회원가입 방식 (이메일, 간편로그인)",
            "activatedAt": "계정 활성화 일시",
            "agreeTerm": "약관 동의 여부",
            "authProvider": "외부 인증 제공자 (예: Google, Facebook)",
            "companyCode": "회사 코드",
            "companyDepartment": "회사 부서",
            "companyEmployeeNumber": "사번",
            "companyName": "회사명",
            "companySK": "회사 세부 식별자 (Sort Key)",
            "createdAt": "생성 일시",
            "dataType": "데이터 유형",
            "email": "이메일 주소",
            "engName": "영문 이름",
            "engNation": "영문 국적",
            "estimate": "견적 금액",
            "estimateFile": "견적서 파일 참조",
            "finishAt": "서비스 종료 일시",
            "gender": "성별",
            "groupKey": "그룹 식별 키",
            "groupName": "그룹 이름",
            "idNumber": "신분증 번호 또는 주민등록번호",
            "insuranceCertificateUrl": "보험 증명서 URL",
            "insuranceEndDate": "보험 종료일",
            "insuranceEvacuationPlan": "보험 포함 대피 계획",
            "insurancePlan": "보험 플랜 종류",
            "insuranceStartDate": "보험 시작일",
            "linkPaperGuide": "종이 신청서 가이드 링크",
            "linkPaperJoin": "종이 신청서 접수 링크",
            "linkPaperJoinEng": "종이 신청서 접수 링크 (영문)",
            "managerEmail": "담당자 이메일",
            "managerName": "담당자 이름",
            "managerTel": "담당자 전화번호",
            "membershipCertificateUrl": "기업멤버십 가입증명서 URL",
            "membershipCorporateType": "기업멤버십 유형",
            "membershipEndDate": "기업멤버십 종료일",
            "membershipPersonalType": "기업멤버십 개인 유형",
            "membershipStartDate": "기업멤버십 시작일",
            "name": "이름",
            "nation": "국가",
            "paidAt": "결제 일시",
            "paidPrice": "결제 금액",
            "period": "이용 기간",
            "policyNumber": "보험 증권 번호",
            "price": "기본 금액",
            "productName": "상품명",
            "productSk": "상품 세부 식별자 (SK)",
            "receipts": "영수증 목록 또는 파일 참조",
            "registrationCount": "등록 횟수",
            "registrationNumber": "등록 번호",
            "residenceBusinessTripType": "체류 유형 (거주/출장)",
            "residenceCityCode": "거주 도시 코드",
            "residenceCountryCode": "거주 국가 코드",
            "residenceCountryName": "거주 국가명",
            "residenceEndDate": "거주 종료일",
            "residenceStartDate": "거주 시작일",
            "residenceStayType": "거주 형태 (단기/장기 등)",
            "startAt": "시작 일시",
            "status": "상태 (예: 활성, 만료)",
            "tel": "전화번호",
            "timestamp": "타임스탬프 (Unix epoch)",
            "totalPrice": "총 금액",
            "trainingInfo": "교육 정보",
            "updatedAt": "수정 일시",
            "userBirthDate": "사용자 생년월일",
            "userEmail": "사용자 이메일 주소",
            "userEmergencyContact": "긴급 연락처",
            "userEnglishName": "사용자 영문 이름",
            "userGender": "사용자 성별",
            "userName": "사용자 실명",
            "userNote": "사용자 메모",
            "userPhone": "사용자 전화번호",
            "userRegistrationNumber": "사용자 등록번호 또는 신분증 번호",
            "userRelation": "신청자와의 관계 (본인, 배우자 등)",
            "userType": "사용자 유형 (관리자, 일반, 게스트 등)"
        }
    }

@mcp.tool()
def scan_table(filters: Optional[Dict[str, Dict[str, str]]] = None, start_key: Optional[dict] = None, limit: Optional[int] = 10) -> dict:
    """
    Scan the DynamoDB table with optional filters and start_key for pagination.
    Returns up to the specified limit of items per call after filtering.

    Parameters:
    - filters: Dictionary of attribute conditions using the format:
        {
            "attributeName": {"operator": "value"}
        }
        Supported operators:
        - eq: Equal to
        - ne: Not equal to
        - lt: Less than
        - lte: Less than or equal to
        - gt: Greater than
        - gte: Greater than or equal to
        - begins_with: Starts with the specified value
        - contains: Contains the specified value
        - between: Between two values - {"between": ["value1", "value2"]}
        - in: In a list of values - {"in": ["value1", "value2", "value3"]}
        - exists: Attribute exists - {"exists": true}
        - not_exists: Attribute does not exist - {"not_exists": true}
    - start_key: Start key for pagination (from lastEvaluatedKey).
    - limit: Maximum number of items to return (default 10). Max value is 100.

    Returns:
    - items: Array of matching items from the table.
    - lastEvaluatedKey: Pagination token for getting the next set of results.
    - count: Number of items returned in this response.
    - scannedCount: Total number of items scanned before filtering.

    Note:
    - If lastEvaluatedKey is present in the response, more results are available.
      You can retrieve these by passing this value as the start_key in a subsequent call.
    - Results are formatted as a table for better readability.
    
    Examples:
    # Equal condition - find items where name is "John"
    filters = {"name": {"eq": "John"}}
    
    # Multiple conditions - find items where age >= 30 AND job is "Developer"
    filters = {
        "age": {"gte": 30},
        "job": {"eq": "Developer"}
    }
    
    # Range search - find items where age is between 20 and 30
    filters = {"age": {"between": [20, 30]}}
    
    # Contains search - find items where hobbies list contains "Reading"
    filters = {"hobbies": {"contains": "Reading"}}
    """
    scan_kwargs = {}
    
    # 필터 조건 구성
    if filters:
        condition = None
        for key, condition_dict in filters.items():
            for operator, value in condition_dict.items():
                expr = None
                
                # 지원하는 연산자별 조건식 생성
                if operator == 'eq':
                    expr = Attr(key).eq(value)
                elif operator == 'ne':
                    expr = Attr(key).ne(value)
                elif operator == 'lt':
                    expr = Attr(key).lt(value)
                elif operator == 'lte':
                    expr = Attr(key).lte(value)
                elif operator == 'gt':
                    expr = Attr(key).gt(value)
                elif operator == 'gte':
                    expr = Attr(key).gte(value)
                elif operator == 'begins_with':
                    expr = Attr(key).begins_with(value)
                elif operator == 'contains':
                    expr = Attr(key).contains(value)
                elif operator == 'between' and isinstance(value, list) and len(value) == 2:
                    expr = Attr(key).between(value[0], value[1])
                elif operator == 'in' and isinstance(value, list):
                    expr = Attr(key).is_in(value)
                elif operator == 'exists' and value:
                    expr = Attr(key).exists()
                elif operator == 'not_exists' and value:
                    expr = Attr(key).not_exists()
                
                # 생성된 표현식을 기존 조건과 AND로 결합
                if expr:
                    condition = expr if condition is None else condition & expr
                
        # 필터 표현식 설정
        if condition:
            scan_kwargs["FilterExpression"] = condition

    # 페이지네이션 키 적용
    if start_key:
        scan_kwargs["ExclusiveStartKey"] = start_key

    # DynamoDB 스캔 - AWS 콘솔과 같이 모든 데이터를 스캔하고 필터링
    response = table.scan(**scan_kwargs)
    
    # 사용자가 지정한 limit 값 사용 (최대 100개로 제한)
    actual_limit = min(limit, 100) if limit is not None else 10
    
    # 필터링 후 결과에서 지정된 개수만 반환
    items = response.get("Items", [])[:actual_limit]
    
    return {
        "items": items,
        "lastEvaluatedKey": response.get("LastEvaluatedKey"),
        "count": len(items),
        "scannedCount": response.get("ScannedCount", 0)
    }

if __name__ == "__main__":
    mcp.run()
