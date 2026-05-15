# 编排器-子模块接口规范（v20.3）

> **用途**：定义模式编排器与子模块之间的标准输入/输出schema，确保模块间数据传递的一致性和可维护性。

---

## 一、通用接口契约

### 1.1 编排器→子模块（输入）

```yaml
interface OrchestratorToSubmodule:
  context:
    project_name: string          # 项目名称
    current_mode: string          # 当前模式标识（A/B/B-2/C/D/E/F）
    previous_output: object       # 前一阶段/模块的输出数据
    user_preferences: object      # 用户偏好设置（来自preferences.md）
  parameters:
    trigger_type: enum            # 触发类型：auto | manual | scheduled
    scope: string                 # 作用范围（如：章节编号、诊断对象）
    options: object               # 可选参数（如：深度、格式偏好）
  constraints:
    max_output_length: number     # 最大输出长度限制
    required_fields: list         # 必须返回的字段列表
    timeout: number               # 超时限制（秒）
```

### 1.2 子模块→编排器（输出）

```yaml
interface SubmoduleToOrchestrator:
  status:
    code: enum                    # success | partial | error
    message: string               # 状态描述
  data:
    result: object                # 核心输出数据
    metadata: object              # 元数据（版本、时间戳、数据来源）
  diagnostics:
    warnings: list                # 警告信息列表
    suggestions: list             # 建议操作列表
  next_actions:
    recommended: list             # 推荐的下一步操作
    required: list                # 必须执行的后续操作
```

---

## 二、模式B（大纲生成）接口

### 2.1 编排器→子模块

| 子模块 | 输入字段 | 类型 | 必填 | 说明 |
|--------|---------|------|:---:|------|
| literary-mode.md | `outline_data` | object | ✅ | 当前大纲完整数据 |
| literary-mode.md | `literary_style` | enum | ❌ | 文学风格选择 |
| test-cases.md | `outline_data` | object | ✅ | 当前大纲完整数据 |
| test-cases.md | `test_type` | enum | ✅ | 测试类型（玄幻/都市/言情/悬疑/科幻） |
| test-cases.md | `complexity` | enum | ✅ | 复杂度（基础/进阶/高级） |

### 2.2 子模块→编排器

| 子模块 | 输出字段 | 类型 | 说明 |
|--------|---------|------|------|
| literary-mode.md | `enhanced_outline` | object | 文学性增强后的大纲 |
| literary-mode.md | `symbol_system` | object | 象征体系设计 |
| literary-mode.md | `narrative_aesthetics` | object | 叙事美学方案 |
| test-cases.md | `test_results` | list | 测试用例执行结果 |
| test-cases.md | `coverage_report` | object | 大纲覆盖度报告 |

---

## 三、模式B-2（细纲生成）接口

### 3.1 编排器→子模块

| 子模块 | 输入字段 | 类型 | 必填 | 说明 |
|--------|---------|------|:---:|------|
| detailed-outline-core.md | `outline_data` | object | ✅ | 大纲完整数据 |
| detailed-outline-core.md | `chapter_range` | object | ✅ | 章节范围（start, end） |
| detailed-outline-core.md | `volume_info` | object | ✅ | 卷信息（卷号、卷名） |
| template-library.md | `template_type` | enum | ✅ | 模板类型选择 |

### 3.2 子模块→编排器

| 子模块 | 输出字段 | 类型 | 说明 |
|--------|---------|------|------|
| detailed-outline-core.md | `detailed_outline` | list | 逐章细纲数据 |
| detailed-outline-core.md | `conflict_tracking` | object | 冲突追踪表 |
| detailed-outline-core.md | `milestone_map` | object | 高潮/结局里程碑 |
| template-library.md | `template_config` | object | 模板配置参数 |

---

## 四、模式C（正文创作）接口

### 4.1 编排器→子模块

| 子模块 | 输入字段 | 类型 | 必填 | 说明 |
|--------|---------|------|:---:|------|
| writing-workflow.md | `project_config` | object | ✅ | 项目配置（首次加载） |
| chapter-openings.md | `chapter_context` | object | ✅ | 当前章节上下文 |
| hook-techniques.md | `chapter_context` | object | ✅ | 当前章节上下文 |
| scene-techniques.md | `scene_type` | enum | ✅ | 场景类型 |
| character-dialogue.md | `character_data` | object | ✅ | 角色数据 |
| character-dialogue.md | `dialogue_context` | object | ✅ | 对话上下文 |
| version-management.md | `chapter_id` | string | ✅ | 章节标识 |
| version-management.md | `action` | enum | ✅ | 操作类型（对比/回退/分支） |
| reader-preview.md | `chapter_content` | string | ✅ | 章节正文内容 |

### 4.2 子模块→编排器

| 子模块 | 输出字段 | 类型 | 说明 |
|--------|---------|------|------|
| writing-workflow.md | `workflow_config` | object | 写作流程配置 |
| chapter-openings.md | `opening_text` | string | 章节开头文本 |
| hook-techniques.md | `hook_text` | string | 钩子文本 |
| scene-techniques.md | `enhanced_scene` | string | 增强后的场景描写 |
| character-dialogue.md | `dialogue_text` | string | 对话文本 |
| version-management.md | `version_data` | object | 版本数据 |
| reader-preview.md | `preview_report` | object | 读者预览报告 |

---

## 五、模式E（统一诊断中心）接口

### 5.1 编排器→子模块

| 子模块 | 输入字段 | 类型 | 必填 | 说明 |
|--------|---------|------|:---:|------|
| diagnosis-details.md | `diagnosis_target` | object | ✅ | 诊断目标（大纲/细纲/正文） |
| diagnosis-details.md | `diagnosis_dimensions` | list | ❌ | 指定诊断维度（默认全部） |
| cross-volume-rhythm.md | `volume_data` | list | ✅ | 各卷数据 |
| reader-visualization.md | `chapter_content` | string | ✅ | 章节内容 |
| batch-auto-fix.md | `target_list` | list | ✅ | 批量诊断目标列表 |
| batch-auto-fix.md | `fix_level` | enum | ✅ | 修复级别（P0/P1/P2） |
| outline-plot-deep-diagnosis.md | `outline_data` | object | ✅ | 大纲数据 |
| outline-plot-deep-diagnosis.md | `platform_standard` | enum | ✅ | 平台标准（起点/番茄/晋江/纵横） |
| dashboard.md | `project_data` | object | ✅ | 项目全量数据 |
| outline-diagnostics/* | `outline_data` | object | ✅ | 大纲数据 |
| detailed-outline-diagnostics/* | `detailed_outline_data` | object | ✅ | 细纲数据 |
| writing-diagnostics/* | `chapter_data` | object | ✅ | 章节数据 |

### 5.2 子模块→编排器

| 子模块 | 输出字段 | 类型 | 说明 |
|--------|---------|------|------|
| diagnosis-details.md | `diagnosis_report` | object | 14维诊断报告 |
| diagnosis-details.md | `issue_list` | list | 问题清单（含优先级） |
| cross-volume-rhythm.md | `rhythm_report` | object | 跨卷节奏报告 |
| reader-visualization.md | `reader_simulation` | object | 读者模拟结果 |
| batch-auto-fix.md | `fix_report` | object | 批量修复报告 |
| outline-plot-deep-diagnosis.md | `deep_diagnosis_report` | object | 深度诊断报告 |
| dashboard.md | `dashboard_data` | object | 仪表板数据 |
| outline-diagnostics/* | `outline_diagnosis` | object | 大纲诊断结果 |
| detailed-outline-diagnostics/* | `detailed_outline_diagnosis` | object | 细纲诊断结果 |
| writing-diagnostics/* | `writing_diagnosis` | object | 正文诊断结果 |

---

## 六、模式D（包装运营）接口

### 6.1 编排器→子模块

| 功能模块 | 输入字段 | 类型 | 必填 | 说明 |
|---------|---------|------|:---:|------|
| 书名优化 | `work_info` | object | ✅ | 作品基本信息 |
| 简介打磨 | `work_info` | object | ✅ | 作品基本信息 |
| 简介打磨 | `target_platform` | enum | ✅ | 目标平台 |
| 标签SEO | `work_info` | object | ✅ | 作品基本信息 |
| 封面文案 | `work_info` | object | ✅ | 作品基本信息 |
| 竞品分析 | `work_info` | object | ✅ | 作品基本信息 |
| 竞品分析 | `competitor_count` | number | ❌ | 竞品数量（默认5） |
| 转化率预估 | `synopsis_text` | string | ✅ | 简介文本 |
| 转化率预估 | `target_platform` | enum | ✅ | 目标平台 |
| 书名A/B测试 | `title_list` | list | ✅ | 书名候选列表 |
| 书名A/B测试 | `target_platforms` | list | ✅ | 目标平台列表 |

### 6.2 子模块→编排器

| 功能模块 | 输出字段 | 类型 | 说明 |
|---------|---------|------|------|
| 书名优化 | `title_proposals` | list | 书名方案列表 |
| 简介打磨 | `synopsis_proposals` | list | 简介方案列表 |
| 标签SEO | `tag_combinations` | list | 标签组合方案 |
| 封面文案 | `cover_copy` | list | 封面文案列表 |
| 竞品分析 | `competitor_report` | object | 竞品分析报告 |
| 转化率预估 | `conversion_report` | object | 转化率预估报告 |
| 书名A/B测试 | `ab_test_matrix` | object | A/B测试矩阵 |

---

## 七、模式F（全自动流水线）接口

### 7.1 编排器→各阶段

```yaml
interface PipelineToStage:
  stage_config:
    stage_id: number              # 阶段编号（0-7）
    stage_name: string            # 阶段名称
    target_mode: enum             # 目标模式（A/B/B-2/C/E/D）
    input_data: object            # 上游阶段输出数据
  pipeline_state:
    total_stages: number          # 总阶段数
    completed_stages: list        # 已完成阶段列表
    checkpoint_data: object       # 断点数据（用于恢复）
  execution_options:
    batch_mode: boolean           # 是否批量模式
    parallel_mode: boolean        # 是否并行模式
    auto_continue: boolean        # 是否自动继续
```

### 7.2 各阶段→编排器

```yaml
interface StageToPipeline:
  stage_result:
    status: enum                  # success | partial | error
    output_data: object           # 阶段输出数据
    artifacts: list               # 生成的文件列表
  checkpoint:
    save_point: object            # 断点保存数据
    can_resume: boolean           # 是否可从此处恢复
  metrics:
    duration: number              # 阶段耗时（秒）
    quality_score: number         # 质量评分
    retry_count: number           # 重试次数
```

---

## 八、错误处理规范

### 8.1 错误码定义

| 错误码 | 含义 | 处理方式 |
|:---:|------|---------|
| E001 | 输入数据缺失必填字段 | 返回错误，提示缺失字段 |
| E002 | 输入数据格式不匹配 | 返回错误，提示期望格式 |
| E003 | 子模块执行超时 | 重试1次，仍失败则降级处理 |
| E004 | 子模块返回数据不完整 | 标记partial状态，补充默认值 |
| E005 | 依赖数据版本不兼容 | 提示版本升级或数据迁移 |
| E006 | 外部资源不可用 | 使用缓存数据或跳过该步骤 |

### 8.2 降级策略

| 场景 | 降级方案 | 影响 |
|------|---------|------|
| 子模块加载失败 | 使用内置默认逻辑 | 功能简化，核心流程不受影响 |
| 诊断模块不可用 | 跳过诊断，标记待补 | 质量保障暂时缺失 |
| 数据总线写入失败 | 使用本地缓存 | 跨模块数据共享暂时中断 |
| Memory更新失败 | 降级为文件保存 | 状态恢复能力下降 |

---

## 九、版本兼容性

### 9.1 接口版本号规则

```
接口版本号格式：v[主版本].[次版本]
- 主版本变更：不兼容的接口修改（字段删除、类型变更）
- 次版本变更：向后兼容的接口扩展（新增可选字段）
```

### 9.2 当前接口版本

| 模式 | 编排器版本 | 接口版本 | 兼容范围 |
|------|:---:|:---:|------|
| 模式A | v20.3 | v1.0 | v1.0+ |
| 模式B | v20.3 | v1.0 | v1.0+ |
| 模式B-2 | v20.3 | v1.0 | v1.0+ |
| 模式C | v20.3 | v1.0 | v1.0+ |
| 模式D | v20.3 | v1.0 | v1.0+ |
| 模式E | v20.3 | v1.0 | v1.0+ |
| 模式F | v20.3 | v1.0 | v1.0+ |