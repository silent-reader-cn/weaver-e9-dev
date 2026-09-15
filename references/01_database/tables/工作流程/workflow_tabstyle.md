# 泛微OA 数据表: `workflow_tabstyle`

- **所属模块**: `工作流程`
- **数据库表名**: `workflow_tabstyle`
- **字段总数**: `25`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `styleid` | 样式id | `integer` | - | 否 | - |
| 2 | `stylename` | 样式名称 | `varchar2` | 1000 | 是 | - |
| 3 | `image_bg` | 背景图片 | `varchar2` | 1000 | 是 | - |
| 4 | `image_sep` | 分隔图片 | `varchar2` | 1000 | 是 | - |
| 5 | `image_sepwidth` | 分隔图片宽度 | `integer` | - | 是 | - |
| 6 | `sel_bgleft` | 背景图-左，选中 | `varchar2` | 1000 | 是 | - |
| 7 | `sel_bgleftwidth` | 背景图宽度-左，选中 | `integer` | - | 是 | - |
| 8 | `sel_bgmiddle` | 背景图-居中，选中 | `varchar2` | 1000 | 是 | - |
| 9 | `sel_bgright` | 背景图-右，选中 | `varchar2` | 1000 | 是 | - |
| 10 | `sel_bgrightwidth` | 背景图宽度-右，选中 | `integer` | - | 是 | - |
| 11 | `sel_color` | 选中颜色 | `varchar2` | 400 | 是 | - |
| 12 | `sel_fontsize` | 选中字体大小 | `integer` | - | 是 | - |
| 13 | `sel_family` | 选中类 | `varchar2` | 400 | 是 | - |
| 14 | `sel_bold` | 选中粗体 | `integer` | - | 是 | - |
| 15 | `sel_italic` | 选中斜体 | `integer` | - | 是 | - |
| 16 | `unsel_bgleft` | 背景图-左，未选中 | `varchar2` | 1000 | 是 | - |
| 17 | `unsel_bgleftwidth` | 背景图宽度-左，未选中 | `integer` | - | 是 | - |
| 18 | `unsel_bgmiddle` | 背景图-居中，未选中 | `varchar2` | 1000 | 是 | - |
| 19 | `unsel_bgright` | 背景图-右，未选中 | `varchar2` | 1000 | 是 | - |
| 20 | `unsel_bgrightwidth` | 背景图宽度-右，未选中 | `integer` | - | 是 | - |
| 21 | `unsel_color` | 未选中颜色 | `varchar2` | 400 | 是 | - |
| 22 | `unsel_fontsize` | 未选中字体大小 | `integer` | - | 是 | - |
| 23 | `unsel_family` | 未选中类 | `varchar2` | 400 | 是 | - |
| 24 | `unsel_bold` | 未选中粗体 | `integer` | - | 是 | - |
| 25 | `unsel_italic` | 未选中斜体 | `integer` | - | 是 | - |
