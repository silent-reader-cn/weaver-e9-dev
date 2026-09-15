# 泛微OA 数据表: `prj_template`

- **所属模块**: `项目管理`
- **数据库表名**: `prj_template`
- **字段总数**: `39`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 标识id | `integer` | - | 否 | 标识列 |
| 2 | `isselected` | 是否指定 | `char` | 1 | 是 | 是否指定 |
| 3 | `templetname` | 模板名称 | `varchar2` | 400 | 是 | 模板名称 |
| 4 | `templetdesc` | 描述 | `varchar2` | 1000 | 是 | 描述 |
| 5 | `protypeid` | 项目类型 | `integer` | - | 是 | 项目类型 |
| 6 | `worktypeid` | 工作类型 | `integer` | - | 是 | 工作类型 |
| 7 | `promember` | 项目成员 | `varchar2` | 1000 | 是 | 项目成员 |
| 8 | `ismembersee` | 成员可见 | `char` | 1 | 是 | 成员可见 |
| 9 | `procrm` | 相关客户 | `varchar2` | 1000 | 是 | 相关客户 |
| 10 | `iscrmsee` | 客户可见 | `char` | 1 | 是 | 客户可见 |
| 11 | `parentproid` | 上级项目 | `integer` | - | 是 | 上级项目 |
| 12 | `commentdoc` | 评价书 | `integer` | - | 是 | 评价书 |
| 13 | `confirmdoc` | 确认书 | `integer` | - | 是 | 确认书 |
| 14 | `advicedoc` | 建议书 | `integer` | - | 是 | 建议书 |
| 15 | `manager` | 项目经理 | `integer` | - | 是 | 项目经理 |
| 16 | `datefield1` | 自定义日期字段1 | `varchar2` | 80 | 是 | 自定义日期字段1 |
| 17 | `datefield2` | 自定义日期字段2 | `varchar2` | 80 | 是 | 自定义日期字段2 |
| 18 | `datefield3` | 自定义日期字段3 | `varchar2` | 80 | 是 | 自定义日期字段3 |
| 19 | `datefield4` | 自定义日期字段4 | `varchar2` | 80 | 是 | 自定义日期字段4 |
| 20 | `datefield5` | 自定义日期字段5 | `varchar2` | 80 | 是 | 自定义日期字段5 |
| 21 | `numberfield1` | 自定义数字字段1 | `float` | 22 | 是 | 自定义数字字段1 |
| 22 | `numberfield2` | 自定义数字字段2 | `float` | 22 | 是 | 自定义数字字段2 |
| 23 | `numberfield3` | 自定义数字字段3 | `float` | 22 | 是 | 自定义数字字段3 |
| 24 | `numberfield4` | 自定义数字字段4 | `float` | 22 | 是 | 自定义数字字段4 |
| 25 | `numberfield5` | 自定义数字字段5 | `float` | 22 | 是 | 自定义数字字段5 |
| 26 | `textfield1` | 自定义文本字段1 | `varchar2` | 800 | 是 | 自定义文本字段1 |
| 27 | `textfield2` | 自定义文本字段2 | `varchar2` | 800 | 是 | 自定义文本字段2 |
| 28 | `textfield3` | 自定义文本字段3 | `varchar2` | 800 | 是 | 自定义文本字段3 |
| 29 | `textfield4` | 自定义文本字段4 | `varchar2` | 800 | 是 | 自定义文本字段4 |
| 30 | `textfield5` | 自定义文本字段5 | `varchar2` | 800 | 是 | 自定义文本字段5 |
| 31 | `tinyintfield1` | 自定义选择字段1 | `integer` | - | 是 | 自定义选择字段1 |
| 32 | `tinyintfield2` | 自定义选择字段2 | `integer` | - | 是 | 自定义选择字段2 |
| 33 | `tinyintfield3` | 自定义选择字段3 | `integer` | - | 是 | 自定义选择字段3 |
| 34 | `tinyintfield4` | 自定义选择字段4 | `integer` | - | 是 | 自定义选择字段4 |
| 35 | `tinyintfield5` | 自定义选择字段5 | `integer` | - | 是 | 自定义选择字段5 |
| 36 | `status` | 状态 | `char` | 1 | 是 | 状态 |
| 37 | `relationxml` | wbs任务关系 | `long` | 0 | 是 | wbs任务关系(e8已弃用该字段) |
| 38 | `updatedate` | 更新日期 | `char` | 10 | 是 | 更新日期 |
| 39 | `accessory` | 附件 | `varchar2` | 2000 | 是 | 附件 |
