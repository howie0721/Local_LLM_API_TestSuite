# Changelog

本文件記錄專案所有重要變更，遵循 [Keep a Changelog](https://keepachangelog.com/) 格式。

## [Unreleased]

### Planned
- Stability testing implementation
- Usability testing framework
- Performance baseline establishment
- Multi-model comparison testing

---

## [1.0.0] - 2025-11-04

### Added
- ✅ Complete test framework with 38 test files
- ✅ Pytest markers for test categorization (9 categories)
- ✅ CI/CD workflows (PR tests, nightly tests, manual tests)
- ✅ GitHub Actions integration with Docker Ollama
- ✅ Allure reporting with GitHub Pages deployment
- ✅ Comprehensive documentation (20+ files)
- ✅ Test pyramid structure (Unit → Boundary → Integration → E2E)
- ✅ JMeter performance testing scripts
- ✅ Security testing suite (injection, data leakage, auth)
- ✅ Multi-language support testing (EN, ZH, JA, KO)

### Test Coverage
- Unit tests: 6 files
- Boundary tests: 6 files
- Compatibility tests: 4 files
- Error handling tests: 2 files
- Integration tests: 5 files
- E2E tests: 5 files
- Regression tests: 5 files
- Security tests: 5 files

### CI/CD
- PR workflow: Fast tests (unit + boundary + compatibility + error_handling) ~5-10 min
- Nightly workflow: Full suite (e2e + regression + security + integration + usability) ~20-30 min
- Manual workflow: On-demand testing with customizable parameters

### Documentation
- Architecture.md: System design and structure
- Test_Strategy.md: Test approach and methodologies
- How_To_Run.md: Execution guide
- 3rd_Party_Tools.md: Tool stack documentation
- Contributing.md: Contribution guidelines
- FAQ.md: 27 Q&A for common issues
- CI_CD_Setup_Guide.md: CI/CD configuration
- Allure_Report_Guide.md: Reporting framework guide
- Coding_Style_Guide.md: Code standards
- Glossary.md: Technical terms
- Test_Pyramid.md: Test distribution strategy
- Troubleshooting.md: Common problems and solutions
- And more...

---

## [0.3.0] - 2025-11-03

### Added
- Security testing suite
  - Injection attack testing
  - Sensitive data protection
  - Authentication/Authorization testing
  - Data leakage prevention

### Changed
- Reorganized test structure by category
- Updated pytest.ini with all markers
- Enhanced conftest.py with shared fixtures

---

## [0.2.0] - 2025-11-02

### Added
- Integration testing suite
  - Multi-turn conversation testing
  - Context retention validation
  - Streaming integration
  - Model switching

- E2E testing suite
  - User scenario testing
  - Real-world prompt testing
  - Complete workflow validation

### Changed
- Improved test data fixtures
- Enhanced error handling in tests

---

## [0.1.0] - 2025-11-01

### Added
- Initial test framework setup
- Unit tests for basic functionality
  - Connection testing
  - Model info retrieval
  - Helper functions
  - Prompt validation
  - Response parsing
  - Timeout handling

- Boundary tests
  - Prompt length boundaries
  - Special character handling
  - Numeric boundaries
  - Concurrent limits
  - Token limits
  - Empty input handling

- Compatibility tests
  - Multi-language support
  - Model compatibility
  - OS compatibility

- Error handling tests
  - Error response handling
  - Invalid input testing

### Infrastructure
- Pytest configuration
- Basic fixtures in conftest.py
- Test data in JSON format
- Helper utilities

---

## Release History

| Version | Date | Summary |
|---------|------|---------|
| 1.0.0 | 2025-11-04 | Complete framework with CI/CD, documentation |
| 0.3.0 | 2025-11-03 | Security testing suite |
| 0.2.0 | 2025-11-02 | Integration & E2E testing |
| 0.1.0 | 2025-11-01 | Initial framework |

---

## Semantic Versioning

本專案遵循 [Semantic Versioning](https://semver.org/)：

- **MAJOR** (1.x.x): 不相容的 API 變更
- **MINOR** (x.1.x): 向後相容的新功能
- **PATCH** (x.x.1): 向後相容的錯誤修復

---

## Contributing to Changelog

當您提交 PR 時，請在 `[Unreleased]` 區段加入您的變更：

```markdown
## [Unreleased]

### Added
- 新增 XXX 測試
- 新增 YYY 功能

### Changed
- 修改 ZZZ 測試邏輯

### Fixed
- 修復 AAA bug
```

**類別說明**:
- **Added**: 新功能
- **Changed**: 現有功能的變更
- **Deprecated**: 即將移除的功能
- **Removed**: 已移除的功能
- **Fixed**: Bug 修復
- **Security**: 安全性相關變更

---

**維護者**: @howie0721  
**最後更新**: 2025-11-04
