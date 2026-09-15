# 泛微OA 数据表: `modetreefield`

- **所属模块**: `表单建模`
- **数据库表名**: `modetreefield`
- **字段总数**: `13`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `icon` | 应用自定义图标 | `varchar2` | 50 | 是 | - |
| 2 | `iconcolor` | 图标字体颜色 | `varchar2` | 20 | 是 | - |
| 3 | `iconbg` | 图标背景颜色 | `varchar2` | 20 | 是 | - |
| 4 | `id` | 应用id | `integer` | - | 是 | - |
| 5 | `treefieldname` | 应用名称 | `varchar2` | 640 | 是 | 应用名称 |
| 6 | `superfieldid` | 上级应用 | `integer` | - | 是 | 上级应用的id，对应本表中的id字段 |
| 7 | `allsuperfieldid` | 所有上级应用 | `varchar2` | 640 | 是 | 所有上级应用的id,以英文逗号隔开,对应本表中的id字段 |
| 8 | `treelevel` | 应用级别 | `integer` | - | 是 | 应用级别，根应用对应级别0，下一级对应1，以此类推 |
| 9 | `islast` | 是否末节 | `char` | 1 | 是 | 1、是；0：不是(作废) |
| 10 | `showorder` | 显示顺序 | `number` | (15,2) | 是 | 显示顺序，两位小数 |
| 11 | `treefielddesc` | 描述 | `varchar2` | 1000 | 是 | 描述信息 |
| 12 | `isdelete` | 是否逻辑删除 | `integer` | - | 是 | 0：未删除；1：已删除 |
| 13 | `subcompanyid` | 所属分部 | `integer` | - | 是 | 对应表hrmsubcompany中的id字段，用于表单建模分权功能 |
