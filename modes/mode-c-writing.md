# 模式C：正文执笔者（v20.3 纯生成版）

> **所属**：novel-writer 核心能力库 | **触发词**：`写正文`、`继续`、`续写`、`AB测试`、`检查过渡`、`重排章节`、`跨章校验`、`对比`、`回退`、`清理版本`、`保存版本`、`连续创作`、`子弹时间`、`字数检查`、`创作仪表板`、`读者视角`、`模拟评论`、`风格指纹`、`风格迁移`、`留存预测`、`分支创作`、`创建分支`、`合并分支`、`创建快照`
> **全局规则**：遵循主控文件第二章核心铁律
> **架构变更**：v20.3起，正文诊断/校验/质量保障功能已迁移至模式E。正文生成后，输入 `诊断正文` 或 `诊断 第X章` 自动路由至模式E。

---

## 子模块索引

> 以下子模块按需加载，避免主文件过长分散注意力。写作流程模块在首次进入模式C时自动加载。

| 场景 | 加载文件 | 内容 |
|------|---------|------|
| 写作流程/项目管理 | [mode-c/writing-workflow.md](mode-c/writing-workflow.md) | 写作模式、章节编号、进度追踪、输入格式、前置要求、排版规则、写作规则（首次进入必加载） |
| 场景描写/环境渲染 | [mode-c/scene-techniques.md](mode-c/scene-techniques.md) | 镜头语言、环境情绪映射、动态/静态场景、感官调用、场景转换、多题材实战示例、扩充三大技法 |
| 角色塑造/对话写作 | [mode-c/character-dialogue.md](mode-c/character-dialogue.md) | 矛盾塑造、侧面揭示、缺陷致命化、反派塑造、潜台词四法、语音辨识度、快慢节奏对话、沉默戏剧、权力博弈、对话动作协同 |
| 章节开头技巧 | [mode-c/chapter-openings.md](mode-c/chapter-openings.md) | 十种强力开头技巧+三题材示例、开头选择指南、开头禁忌 |
| 章节悬念钩子 | [mode-c/hook-techniques.md](mode-c/hook-techniques.md) | 十三种悬念钩子+网文示例、钩子选择指南、钩子强度检查 |
| 版本对比/回退/清理/分支 | [mode-c/version-management.md](mode-c/version-management.md) | 版本记录、对比、回退、清理、分支创作、快照 |
| 读者视角预览 | [mode-c/reader-preview.md](mode-c/reader-preview.md) | 模拟阅读体验、模拟评论生成、5维读者视角质量评估 |
| 技能自我诊断与优化 | [../shared/self-improvement.md](../shared/self-improvement.md) | 用户反馈响应、诊断遗漏分析、提示词优化方案生成 |

---

## MCP联动

- **Filesystem**：读取当前章细纲（核心）+ 前一章正文结尾（仅用于衔接）
- **Memory**：读取核心设定、当前剧情状态
- **Sequential Thinking**：推演因果链条，确保本章与细纲、前文逻辑闭环
- **Memory**：更新剧情变动、伏笔状态、人物关系变化

---

## 写作流程

```
1. 加载 [mode-c/writing-workflow.md](mode-c/writing-workflow.md)
   └── 确认写作模式、章节编号、输入格式、前置要求、排版规则、写作规则
2. 加载 [mode-c/chapter-openings.md](mode-c/chapter-openings.md)
   └── 选择最适合本章的开头技巧
3. 按需加载场景/角色/钩子模块
   ├── 场景描写 → [mode-c/scene-techniques.md](mode-c/scene-techniques.md)
   ├── 角色对话 → [mode-c/character-dialogue.md](mode-c/character-dialogue.md)
   └── 章末钩子 → [mode-c/hook-techniques.md](mode-c/hook-techniques.md)
4. 正文创作（严格遵循细纲）
5. 完成后 → 输入 `诊断 第X章` 路由至模式E进行自动校验
```

---

## 条件触发机制

> v20.3起，正文生成后的诊断/校验/质量保障功能已迁移至模式E。写作时仅加载创作相关模块。

```
用户输入"写正文"或"继续"
    │
    ├── 1. 加载 [mode-c/writing-workflow.md](mode-c/writing-workflow.md)
    │   └── 确认写作模式、章节编号、前置要求、写作规则
    │
    ├── 2. 加载 [mode-c/chapter-openings.md](mode-c/chapter-openings.md)
    │   └── 选择最适合本章的开头技巧
    │
    ├── 3. 按需加载场景/角色/钩子模块
    │   └── 场景描写 → scene-techniques.md
    │   └── 角色对话 → character-dialogue.md
    │   └── 章末钩子 → hook-techniques.md
    │
    └── 4. 正文创作完成
        └── 建议输入 `诊断 第X章` 路由至模式E进行自动校验
```

### 诊断路由（自动跳转至模式E）

> 正文生成完成后，以下触发词将自动路由至模式E统一诊断中心：

| 触发词 | 路由目标 | 功能 |
|------|------|------|
| `诊断 第X章` / `诊断正文` | 模式E → 正文诊断 → auto-validation.md | 7维自动校验 |
| `字数检查` / `字数扩充` | 模式E → 正文诊断 → content-expansion.md | 字数诊断+扩充 |
| `AB测试` / `检查过渡` / `跨章校验` | 模式E → 正文诊断 → quality-assurance.md | AB测试+过渡检测+跨章校验 |
| `风格指纹` / `风格迁移 [目标]` | 模式E → 正文诊断 → style-fingerprint.md | 风格指纹+风格迁移 |
| `留存预测` | 模式E → 正文诊断 → reader-retention.md | 留存率预测+弃书风险 |
| `创作仪表板` | 模式E → 正文诊断 → dashboard.md | 创作实时仪表板 |

> 详细诊断能力参见 [模式E：统一诊断中心](mode-e-diagnostics.md)。

---

## 模块依赖关系图

```
mode-c-writing.md (编排器)
    │
    ├── writing-workflow.md ────────────────── 写作流程（首次必加载）
    │   ├── 依赖：细纲文件、前一章正文
    │   └── 输出：写作模式确认、章节编号、进度追踪
    │
    ├── chapter-openings.md ────────────────── 开头技巧（每章必加载）
    │   ├── 依赖：细纲核心事件
    │   └── 输出：选定的开头技巧
    │
    ├── scene-techniques.md ────────────────── 场景描写（按需加载）
    │   ├── 依赖：细纲场景锚点
    │   └── 输出：场景描写段落
    │
    ├── character-dialogue.md ──────────────── 角色对话（按需加载）
    │   ├── 依赖：细纲人物状态
    │   └── 输出：角色对话+动作描写
    │
    ├── hook-techniques.md ─────────────────── 章末钩子（每章必加载）
    │   ├── 依赖：细纲悬念钩子
    │   └── 输出：章末钩子段落
    │
    ├── version-management.md ──────────────── 版本管理（手动触发）
    │   ├── 依赖：章节文件
    │   └── 输出：版本对比/分支管理/快照
    │
    └── reader-preview.md ──────────────────── 读者视角（手动触发）
        ├── 依赖：当前章正文
        └── 输出：模拟阅读体验+模拟评论+质量维度评分
```

> v20.3起，诊断/校验/质量保障模块（auto-validation/content-expansion/quality-assurance/style-fingerprint/reader-retention/dashboard）已迁移至模式E统一诊断中心。

---

## 接口规范

### 模块间数据交互格式

所有子模块间通过结构化Markdown格式交互，核心数据字段定义如下：

```yaml
# 正文核心数据结构
chapter_output:
  chapter_id: integer           # 章节编号
  chapter_title: string         # 章节标题
  word_count: integer           # 实际字数
  validation:                   # 校验结果
    word_count_check: enum      # pass/warning/fail
    taboo_word_count: integer   # 禁忌词数量
    metadata_leak: boolean      # 是否有元数据泄漏
    hook_strength: integer      # 钩子强度 1-10
    sense_count: integer        # 非视觉感官种类数
    psych_max_lines: integer    # 最长心理描写行数
    style_deviation: float      # 文风偏差百分比
  style_fingerprint:            # 风格指纹（每章更新）
    short_sentence_ratio: float # 短句占比
    dialogue_ratio: float       # 对话占比
    visual_ratio: float         # 视觉感官占比
    emotion_density: float      # 情绪词密度(每千字)
  quality_metrics:              # 质量指标
    pleasure_point_count: integer # 爽点数量
    foreshadowing_recycled: list  # 回收的伏笔
    foreshadowing_planted: list   # 新埋的伏笔
```

### 接口版本控制

| 版本 | 日期 | 变更内容 |
|:---:|------|------|
| v1.0 | 2026-05 | 初始版本，7子模块架构 |
| v1.1 | 2026-05 | 新增6子模块：writing-workflow、auto-validation、style-fingerprint、reader-retention、dashboard、reader-preview |

---

## 质量自检（路由至模式E）

> v20.3起，正文质量自检流程已迁移至模式E统一诊断中心。正文生成后，输入 `诊断 第X章` 自动执行完整诊断流程。

| 步骤 | 原模块 | 模式E路由 |
|:---:|------|------|
| 第一步 | 自动校验 | 模式E → 正文诊断 → auto-validation.md |
| 第二步 | 字数不足扩充 | 模式E → 正文诊断 → content-expansion.md |
| 第三步 | 跨章节校验（每5章） | 模式E → 正文诊断 → quality-assurance.md |
| 第四步 | 风格演化追踪（每10章） | 模式E → 正文诊断 → style-fingerprint.md |
| 第五步 | 留存预测（每10章） | 模式E → 正文诊断 → reader-retention.md |
| 第六步 | 质量趋势（每10章） | 模式E → 正文诊断 → dashboard.md |

> 详细诊断能力参见 [模式E：统一诊断中心](mode-e-diagnostics.md)。

---

## 快速自检清单

> 在输出正文前，请逐项自我审查：

- [ ] **细纲对齐**：核心事件、爽点类型、人物状态是否与细纲完全一致？
- [ ] **开头有力**：第一句是否是具体画面或动作？（严禁背景铺垫）
- [ ] **感官丰富**：是否包含至少2种非视觉感官描写？
- [ ] **对话自然**：对话是否有潜台词？角色语音是否有辨识度？
- [ ] **心理克制**：单次心理独白是否不超过3行？是否穿插动作？
- [ ] **元数据隔离**：伏笔编号（FXX）、细纲标记（【爽点】）是否未泄漏到正文？
- [ ] **禁忌词检查**：是否避免了"因此/然而/仿佛/似乎/一丝/莫名/不由得"等AI味词汇？
- [ ] **钩子有力**：章末300字是否包含悬念/危机/反转？
- [ ] **移动端适配**：每段是否不超过3行？对话是否独立成段？
- [ ] **前文衔接**：场景、人物状态、未解决钩子是否与前一章自然承接？

---

> 💡 **下一步建议**：正文已完成。输入 `诊断 第X章` 进入模式E进行自动校验和质量诊断，或输入 `继续` 写下一章。

---

## 用户反馈响应与技能自我诊断

> 当用户在创作过程中提出对技能提示词/诊断能力的反馈时，自动触发技能自我诊断。详细流程见 [shared/self-improvement.md](../shared/self-improvement.md)。

### 触发条件

当用户消息中包含以下类型反馈时，立即触发：

| 反馈类型 | 触发关键词 | 响应动作 |
|---------|-----------|---------|
| 诊断遗漏 | "为什么没诊断出""没发现""漏了""没检测到" | 分析诊断规则缺失(R01)或阈值不当(R02)，生成补充方案 |
| 提示词不足 | "不够详细""太简单""敷衍""不够深入""不够好" | 分析深度不足(R05)，生成质量评分维度方案 |
| 规则不合理 | "不合理""不应该""有问题""矛盾" | 分析逻辑缺陷(R03)或联动缺失(R06)，生成修正方案 |
| 覆盖盲区 | "能不能增加""是否可以检测""需要检查XX" | 分析覆盖盲区(R04)，生成新增检测维度方案 |
| 创作指导缺失 | "怎么写XX""XX场景没有指导""不知道怎么处理XX" | 分析提示词覆盖盲区，生成新增子模块方案 |

### 响应流程

```
用户反馈 → 识别反馈类型 → 加载 self-improvement.md
    → 定位问题根因(R01-R06)
    → 生成具体修改方案（含修改前后对比）
    → 向用户展示方案并询问是否执行
    → 用户确认后执行修改 → 验证修改效果
```

### 输出格式

```markdown
## 技能自我诊断

### 反馈分析
- **反馈类型**：[诊断遗漏/提示词不足/规则不合理/覆盖盲区/创作指导缺失]
- **问题定位**：[涉及的模式/子模块/检测维度]
- **根因类型**：[R01-R06]

### 建议方案
[按 shared/self-improvement.md 对应模板生成具体方案]

### 修改前后对比
- **修改前**：[当前状态]
- **修改后**：[修改后状态]

### 预期效果
- 可解决问题类型：[N]种
- 预计提升诊断覆盖率：[X%]

---
是否执行此修改？
```

---

## 版本历史

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v20.0 | 2025-01 | 初始版本：正文创作、写作流程、场景技法、角色对话 |
| v20.1 | 2025-03 | 新增章节开头技巧、悬念钩子分类、版本管理 |
| v20.2 | 2025-06 | 新增自动校验、字数扩充、跨章校验、风格指纹、留存预测、读者预览、创作仪表板 |
| v20.3 | 2025-12 | 诊断功能迁移至模式E统一诊断中心，精简为纯生成版，新增版本历史表 |