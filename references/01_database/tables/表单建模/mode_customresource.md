# 泛微OA 数据表: `mode_customresource`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_customresource`
- **字段总数**: `15`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 是 | - |
| 2 | `appid` | 所属应用 | `integer` | - | 是 | 对应modetreefield表的id |
| 3 | `resourcename` | 名称 | `varchar2` | 1000 | 是 | - |
| 4 | `customsearchid` | 查询列表 | `integer` | - | 是 | 对应mode_customsearch表的id |
| 5 | `titlefieldid` | 标题字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 6 | `startdatefieldid` | 开始日期字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 7 | `enddatefieldid` | 结束日期字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 8 | `starttimefieldid` | 开始时间字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 9 | `endtimefieldid` | 结束时间字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 10 | `contentfieldid` | 内容字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 11 | `resourcefieldid` | 资源字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 12 | `resourceshowfieldid` | 资源显示字段 | `integer` | - | 是 | 对应workflow_billfield表的id |
| 13 | `description` | 描述 | `varchar2` | 4000 | 是 | - |
| 14 | `dsporder` | 显示顺序 | `integer` | - | 是 | - |
| 15 | `createurl` | 查询列表链接 | `varchar2` | 1000 | 是 | 当前查询列表的链接 |
