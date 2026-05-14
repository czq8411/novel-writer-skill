# 模式B-2：细纲工程师

> **所属**：novel-writer 核心能力库（模式B子模块） | **触发词**：`细纲`、`章节规划`、`拆解`、`联动优化`、`切换细纲模板`
> **全局规则**：遵循主控文件第二章核心铁律

---

## 子模块索引

> 以下子模块按需加载，避免主文件过长分散注意力。核心输出模板在细纲生成时自动加载。

| 场景 | 加载文件 | 内容 |
|------|---------|------|
| 细纲核心输出 | [mode-b2/detailed-outline-core.md](mode-b2/detailed-outline-core.md) | 输出模板、撰写流程、冲突追踪、高潮/结局里程碑 |
| 质量自动评分 | [mode-b2/quality-scoring.md](mode-b2/quality-scoring.md) | 5维评分体系、评分细则、批量评分汇总 |
| 反向校验 | [mode-b2/reverse-verification.md](mode-b2/reverse-verification.md) | 细纲→大纲合规检查、8项校验、偏离处理 |
| 反向补充 | [mode-b2/reverse-supplement.md](mode-b2/reverse-supplement.md) | 细纲→大纲缺口发现、补充方案生成 |
| 联动优化 | [mode-b2/linkage-optimization.md](mode-b2/linkage-optimization.md) | 多章节爽点轮换、节奏检测、冲突节奏、高潮推进 |
| 模板库 | [mode-b2/template-library.md](mode-b2/template-library.md) | 4类型模板、差异对比、自定义模板 |
| 一致性检查 | [mode-b2/consistency-check.md](mode-b2/consistency-check.md) | 16项一致性检查、变更影响分析 |
| 章节节奏控制 | [mode-b2/chapter-pacing.md](mode-b2/chapter-pacing.md) | 内部/外部冲突追踪、高潮铺垫、结局伏笔、节奏健康度 |
| 大纲反向补充(共享) | [../shared/outline-supplement.md](../shared/outline-supplement.md) | 8维缺口检测、补充方案生成、批量诊断集成 |

---

## MCP联动
- **Memory**：确认前文伏笔、人物当前状态
- **Sequential Thinking**：推演因果链条，确保逻辑闭环
- **Filesystem**：读取前3-5章细纲（确认剧情连续性）+ 读取大纲文件，按模块优先级提取信息（6.3章节摘要→6.2单元→5.2/5.4人物→7.3伏笔→7.1场景），确保细纲与大纲一致

---

## 前置要求

细纲是大纲的**执行级拆解**，必须严格对齐大纲模块（6.1全书结构、6.2剧情节点、6.3章节摘要、5.2主角成长、5.4配角弧线、7.3伏笔管理），并确认与前文的人物状态、伏笔状态、剧情逻辑连续性。

### 撰写流程

1. 读取前3-5章细纲，确认伏笔状态、人物连续性、剧情脉络
2. 按优先级读取大纲：6.3章节摘要 → 6.2单元 → 5.2/5.4人物 → 7.3伏笔 → 7.1场景
3. Sequential Thinking推演因果链
4. 加载 [mode-b2/detailed-outline-core.md](mode-b2/detailed-outline-core.md) 输出模板，逐项填写，每项标注大纲模块编号
5. 一致性自检后通过Filesystem保存

---

## 条件触发机制

> 各子功能模块按条件自动触发，避免全量加载导致注意力分散。

### 细纲生成时（自动触发）

```
用户输入"细纲"或"章节规划"
    │
    ├── 1. 加载 [mode-b2/detailed-outline-core.md](mode-b2/detailed-outline-core.md)
    │   └── 按输出模板生成细纲，自动填充冲突追踪和高潮/结局里程碑
    │
    ├── 2. 细纲输出完成后，自动触发质量评分
    │   └── 加载 [mode-b2/quality-scoring.md](mode-b2/quality-scoring.md)
    │   └── 5维评分，低于阈值自动重写
    │
    ├── 3. 质量评分通过后，自动触发反向校验
    │   └── 加载 [mode-b2/reverse-verification.md](mode-b2/reverse-verification.md)
    │   └── 8项反向校验，严重偏离自动修正
    │
    └── 4. 自动触发一致性检查
        └── 加载 [mode-b2/consistency-check.md](mode-b2/consistency-check.md)
        └── 16项一致性检查，输出检查报告
```

### 累积触发（按章节数自动触发）

| 触发条件 | 加载模块 | 功能 |
|---------|---------|------|
| 每完成5章细纲 | [mode-b2/linkage-optimization.md](mode-b2/linkage-optimization.md) | 多章节联动优化 |
| 每完成10章细纲 | [mode-b2/reverse-supplement.md](mode-b2/reverse-supplement.md) | 大纲反向补充 |
| 每完成10章细纲 | [mode-b2/chapter-pacing.md](mode-b2/chapter-pacing.md) | 节奏健康度评分 |

### 手动触发

| 触发词 | 加载模块 | 功能 |
|--------|---------|------|
| `细纲评分` `细纲评估` `章节评分` | [mode-b2/quality-scoring.md](mode-b2/quality-scoring.md) | 手动质量评分 |
| `反向校验` `细纲校验` `大纲对齐检查` | [mode-b2/reverse-verification.md](mode-b2/reverse-verification.md) | 手动反向校验 |
| `大纲补充` `反向补充大纲` `细纲反馈大纲` | [mode-b2/reverse-supplement.md](mode-b2/reverse-supplement.md) | 手动反向补充 |
| `联动优化` `章节联动` `节奏检测` | [mode-b2/linkage-optimization.md](mode-b2/linkage-optimization.md) | 手动联动优化 |
| `切换细纲模板 [类型]` `细纲模板` `查看模板` | [mode-b2/template-library.md](mode-b2/template-library.md) | 模板管理 |
| `一致性检查` `细纲自检` | [mode-b2/consistency-check.md](mode-b2/consistency-check.md) | 手动一致性检查 |
| `变更影响` `影响分析` | [mode-b2/consistency-check.md](mode-b2/consistency-check.md) | 变更影响分析 |
| `节奏检查` `冲突追踪` `里程碑检查` | [mode-b2/chapter-pacing.md](mode-b2/chapter-pacing.md) | 节奏健康度检查 |

---

## 模块依赖关系图

```
mode-b2-detailed-outline.md (编排器)
    │
    ├── detailed-outline-core.md ───────────── 核心输出（必加载）
    │   ├── 依赖：大纲模块(1-7)、前文章节细纲
    │   └── 输出：章节细纲
    │
    ├── quality-scoring.md ─────────────────── 质量评分（细纲后自动）
    │   ├── 依赖：detailed-outline-core.md 输出
    │   └── 输出：评分报告
    │
    ├── reverse-verification.md ────────────── 反向校验（细纲后自动）
    │   ├── 依赖：detailed-outline-core.md 输出 + 大纲模块(1-7)
    │   └── 输出：偏离清单
    │
    ├── consistency-check.md ───────────────── 一致性检查（细纲后自动）
    │   ├── 依赖：detailed-outline-core.md 输出 + 大纲模块(1-7)
    │   └── 输出：检查报告 + 变更影响分析
    │
    ├── linkage-optimization.md ────────────── 联动优化（每5章自动）
    │   ├── 依赖：最近5章细纲输出
    │   └── 输出：联动优化报告
    │
    ├── reverse-supplement.md ──────────────── 反向补充（每10章自动）
    │   ├── 依赖：shared/outline-supplement.md + 全部细纲
    │   └── 输出：缺口清单 + 补充方案
    │
    ├── chapter-pacing.md ──────────────────── 节奏控制（每10章自动）
    │   ├── 依赖：detailed-outline-core.md 冲突追踪字段 + 大纲1.2.1/6.1.1/6.1.2
    │   └── 输出：节奏健康度评分 + 里程碑总览
    │
    └── template-library.md ────────────────── 模板库（手动触发）
        ├── 依赖：detailed-outline-core.md 输出结构
        └── 输出：模板参数
```

---

## 接口规范

### 模块间数据交互格式

所有子模块间通过结构化Markdown格式交互，核心数据字段定义如下：

```yaml
# 细纲核心数据结构
detailed_outline:
  chapter_id: integer           # 章节编号
  chapter_title: string         # 章节标题
  volume_id: integer            # 所属卷编号
  chapter_function: enum        # 铺垫/发展/高潮/过渡/收尾
  core_event: string            # 核心事件（一句话概括）
  word_count: integer           # 字数
  scene_count: integer          # 场景数
  pleasure_points:              # 爽点
    type: enum                  # 迪化/被动装逼/智商碾压/实力碾压/其他
    intensity: integer          # 1-10
  foreshadowing:                # 伏笔
    recycled: list[F编号]       # 回收的伏笔
    planted: list[F编号]        # 新埋的伏笔
  conflict_tracking:            # 冲突追踪
    internal:                   # 内部冲突
      type: enum                # 想要vs需要/恐惧vs渴望/身份认同/价值观冲突
      stage: enum               # 萌芽期/发展期/激化期/解决期
      progress: float           # 0.0-1.0
    external:                   # 外部冲突
      type: enum                # 人与人/人与势力/人与环境/人与命运
      stage: enum               # 萌芽期/发展期/激化期/决战期
      intensity: integer        # 1-10
  climax_milestone:             # 高潮里程碑
    target_climax: string       # 目标高潮事件
    chapters_remaining: integer # 距高潮章数
    buildup_progress: float     # 铺垫完成度 0.0-1.0
  ending_milestone:             # 结局里程碑
    ending_type: enum           # 圆满/悲壮/开放式/反转/循环
    foreshadowing_count: integer # 已埋结局伏笔数
  outline_references:           # 大纲引用
    - module: string            # 模块编号（如6.3）
      sub_section: string       # 子节编号
      content: string           # 引用内容摘要
```

### 接口版本控制

| 版本 | 日期 | 变更内容 |
|:---:|------|------|
| v1.0 | 2026-05 | 初始版本，7子模块架构 |
| v1.1 | 2026-05 | 新增冲突追踪、高潮/结局里程碑字段 |

---

## 细纲质量自检流程

```
细纲输出完成
    ↓
第一步：质量自动评分（自动）
    └── 加载 [mode-b2/quality-scoring.md](mode-b2/quality-scoring.md)
    └── 5维评分，<7.0自动重写（最多2轮）
    ↓
第二步：反向校验（自动）
    └── 加载 [mode-b2/reverse-verification.md](mode-b2/reverse-verification.md)
    └── 8项反向校验，严重偏离自动修正
    ↓
第三步：一致性检查（自动）
    └── 加载 [mode-b2/consistency-check.md](mode-b2/consistency-check.md)
    └── 16项一致性检查，输出检查报告
    ↓
第四步：联动优化（每5章自动）
    └── 加载 [mode-b2/linkage-optimization.md](mode-b2/linkage-optimization.md)
    └── 5维联动检测，输出优化报告
    ↓
第五步：反向补充（每10章自动）
    └── 加载 [mode-b2/reverse-supplement.md](mode-b2/reverse-supplement.md)
    └── 8维缺口检测，生成补充方案
    ↓
第六步：节奏健康度（每10章自动）
    └── 加载 [mode-b2/chapter-pacing.md](mode-b2/chapter-pacing.md)
    └── 5维节奏评分，输出里程碑总览
```

---

## 快速自检清单

> 在输出细纲前，请逐项自我审查：

- [ ] **大纲对齐**：核心情节是否与大纲6.3章节摘要完全一致？
- [ ] **爽点明确**：爽点类型和强度是否符合大纲要求？配角反应是否设计？
- [ ] **伏笔管理**：回收/埋下伏笔是否与大纲7.3对齐？编号是否正确？
- [ ] **冲突追踪**：内部/外部冲突是否有本章体现？进展是否符合升级路径？
- [ ] **高潮铺垫**：本章是否为卷高潮做了铺垫？铺垫进度是否正常？
- [ ] **结局伏笔**：是否按密度要求埋设结局相关伏笔？
- [ ] **人物一致**：人物状态、关系是否符合大纲当前阶段？
- [ ] **境界约束**：人物境界是否在大纲3.2+5.2约束范围内？
- [ ] **前后衔接**：与前后章的场景、时间线、情绪是否连续？
- [ ] **引用完整**：所有大纲引用是否标注了模块编号和子节编号？

---

> 💡 **下一步建议**：细纲已生成，输入"写正文"开始创作，或输入"细纲"继续规划下一章