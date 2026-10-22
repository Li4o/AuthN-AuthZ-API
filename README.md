# AuthN-AuthZ-API
A secure authentication and authorization API built with Python(FastAPI), featuring JWT, Argon2 hashing, Redis rate-limiting, and OWASP-compliant practtices.

---

## Project Goals
- Webアプリケーションにおける主要なセキュリティリスク(OWASP Top 10等)を理解し、コードレベルで防御対策を実装する。
- 堅牢なトークンベース認証(JWT)・権限管理(RBAC)の仕組みを設計・開発する。
- ソフトウェアエンジニアとして、プロダクションレベルのセキュアコーディングを実践・証明する。

---

## Security Features

### 1. Authentication & Password
- [ ] **ハッシュ化**:　`Argon2` / `bcrypt` によるセキュアなハッシュ化(ソルト・ストレッチング適用)
- [ ] **辞書攻撃・脆弱パスワード対策**: 容易に推測可能な文字列等のパスワードを拒否
- [ ] **JWT トークン認証**: アクセストークン(短期間)とリフレッシュトークンによるステートレスなセッション管理
- [ ] **改ざん検知**: 秘密鍵によるデジタル署名検証

### 2. Authorization
- [ ] **RBAX(Role-Based Access Control)**: 一般ユーザーと管理者権限の厳格なアクセス制御

### 3. Application
- [ ] **Rate Limiting**: `Redis`を用いたIP/ユーザーあたりの連続試行制限
- [ ] **Validation**: Pydanticを使用した型チェックおよび不正フォーマットの遮断
- [ ] **SQLインジェクション対策**: ORM(Prisma / SQLAlchemy)とパラメータ化クエリの徹底

---

## Tech Stack
- **Language**: Python xxx
- **Framework**: FastAPI
- **Databese**: PostgreSQL
- **Cache/Rete Limit**: Redis
- **Container**: Docker /Docker Compose

---

## Directory Structure
> **Coming Soon** ? The directory structure will be updated soon.

---

## Architecture Decisions
- **なぜ JWT の有効期限を短く設定するのか？**
  - ステートレスなJWTのデメリットである「即時無効化の難しさ」をカバーするため、アクセストークンの有効期限を15分程度に抑え、リフレッシュトークンと併用する設計を採用。
- **なぜ Pydantic と ORM を併用するのか？**
  - Pydantic でアプリ入口の入力バリデーションを行い、ORM でDB操作時のクエリ構造化を行うことで、二重のセキュリティ境界を構築するため。