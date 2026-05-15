# 模式B-2：细纲工程师（v20.3 纯生成版）

> **所属**：novel-writer 核心能力库（模式B子模块） | **触发词**：`细纲`、`章节规划`、`拆解`、`切换细纲模板`
> **全局规则**：遵循主控文件第二章核心铁律
> **架构变更**：v20.3起，细纲诊断/评估/优化功能已迁移至模式E。细纲生成后，输入 `诊断细纲` 或 `细纲评分` 自动路由至模式E。

---

## 子模块索引

> 以下子模块按需加载，避免主文件过长分散注意力。核心输出模板在细纲生成时自动加载。

| 场景 | 加载文件 | 内容 |
|------|---------|------|
| 细纲核心输出 | [mode-b2/detailed-outline-core.md](mode-b2/detailed-outline-core.md) | 输出模板、撰写流程、冲突追踪、高潮/结局里程碑 |
| 模板库 | [mode-b2/template-library.md](mode-b2/template-library.md) | 4类型模板、差异对比、自定义模板 |

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

> v20.3起，细纲生成后的诊断/评估/优化功能已迁移至模式E。细纲生成时仅加载核心输出模块。

```
用户输入"细纲"或"章节规划"
    │
    └── 1. 加载 [mode-b2/detailed-outline-core.md](mode-b2/detailed-outline-core.md)
        └── 按输出模板生成细纲，自动填充冲突追踪和高潮/结局里程碑
```

### 诊断路由（自动跳转至模式E）

> 细纲生成完成后，以下触发词将自动路由至模式E统一诊断中心：

| 触发词 | 路由目标 | 功能 |
|------|------|------|
| `细纲评分` / `细纲评估` / `章节评分` | 模式E → 细纲诊断 → quality-scoring.md | 5维细纲质量评分 |
| `反向校验` / `细纲校验` / `大纲对齐检查` | 模式E → 细纲诊断 → reverse-verification.md | 8项反向校验 |
| `一致性检查` / `细纲自检` | 模式E → 细纲诊断 → consistency-check.md | 16项一致性检查 |
| `联动优化` / `章节联动` / `节奏检测` | 模式E → 细纲诊断 → linkage-optimization.md | 5维联动优化 |
| `大纲补充` / `反向补充大纲` / `细纲反馈大纲` | 模式E → 细纲诊断 → reverse-supplement.md | 大纲反向补充 |
| `节奏检查` / `冲突追踪` / `里程碑检查` | 模式E → 细纲诊断 → chapter-pacing.md | 节奏健康度检查 |
| `诊断细纲` | 模式E → 细纲诊断（全模块） | 完整细纲诊断流程 |

> 详细诊断能力参见 [模式E：统一诊断中心](mode-e-diagnostics.md)。

---

## 模块依赖关系图

```
mode-b2-detailed-outline.md (编排器)
    │
    ├── detailed-outline-core.md ───────────── 核心输出（必加载）
    │   ├── 依赖：大纲模块(1-7)、前文章节细纲
    │   └── 输出：章节细纲
    │
    └── template-library.md ────────────────── 模板库（手动触发）
        ├── 依赖：detailed-outline-core.md 输出结构
        └── 输出：模板参数
```

> v20.3起，诊断/评估/优化模块（quality-scoring/reverse-verification/consistency-check/linkage-optimization/reverse-supplement/chapter-pacing）已迁移至模式E统一诊断中心。

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

## 细纲质量自检（路由至模式E）

> v20.3起，细纲质量自检流程已迁移至模式E统一诊断中心。细纲生成后，输入 `诊断细纲` 自动执行完整诊断流程。

| 步骤 | 原模块 | 模式E路由 |
|:---:|------|------|
| 第一步 | 质量自动评分 | 模式E → 细纲诊断 → quality-scoring.md |
| 第二步 | 反向校验 | 模式E → 细纲诊断 → reverse-verification.md |
| 第三步 | 一致性检查 | 模式E → 细纲诊断 → consistency-check.md |
| 第四步 | 联动优化（每5章） | 模式E → 细纲诊断 → linkage-optimization.md |
| 第五步 | 反向补充（每10章） | 模式E → 细纲诊断 → reverse-supplement.md |
| 第六步 | 节奏健康度（每10章） | 模式E → 细纲诊断 → chapter-pacing.md |

> 详细诊断能力参见 [模式E：统一诊断中心](mode-e-diagnostics.md)。

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

> 💡 **下一步建议**：细纲已生成。输入 `诊断细纲` 进入模式E进行质量评分和一致性检查，或输入 `写正文` 开始创作，或输入 `细纲` 继续规划下一章。

---

## 版本历史

| 版本 | 日期 | 变更内容 |
|------|------|---------|
| v20.0 | 2025-01 | 初始版本：章节细纲撰写、模板库 |
| v20.1 | 2025-03 | 新增冲突追踪、高潮/结局里程碑 |
| v20.2 | 2025-06 | 新增质量自动评分、反向校验、一致性检查、联动优化、反向补充、节奏控制 |
| v20.3 | 2025-12 | 诊断功能迁移至模式E统一诊断中心，精简为纯生成版，新增版本历史表 |