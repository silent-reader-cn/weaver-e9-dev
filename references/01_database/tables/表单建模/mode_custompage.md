# 泛微OA 数据表: `mode_custompage`

- **所属模块**: `表单建模`
- **数据库表名**: `mode_custompage`
- **字段总数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `guid` | uuid | `varchar2` | 800 | 是 | - |
| 2 | `props` | 已废弃 | `clob` | 4000 | 是 | 已废弃 |
| 3 | `component` | 已废弃 | `varchar2` | 800 | 是 | 已废弃 |
| 4 | `showorder` | 显示顺序 | `integer` | - | 是 | - |
| 5 | `id` | ID | `integer` | - | 否 | - |
| 6 | `customname` | 名称 | `varchar2` | 1000 | 是 | - |
| 7 | `customdesc` | 描述 | `varchar2` | 1000 | 是 | - |
| 8 | `creater` | 创建人 | `integer` | - | 是 | - |
| 9 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 10 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | - |
| 11 | `appid` | 所属应用 | `integer` | - | 是 | 对应modetreefield表中的id |
