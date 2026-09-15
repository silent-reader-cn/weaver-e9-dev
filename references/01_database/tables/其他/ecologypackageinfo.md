# 泛微OA 数据表: `ecologypackageinfo`

- **所属模块**: `其他`
- **数据库表名**: `ecologypackageinfo`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `label` | 补丁包编号 | `varchar2` | 80 | 是 | - |
| 3 | `name` | 补丁包全称 | `varchar2` | 1000 | 是 | - |
| 4 | `type` | 补丁包类型 | `varchar2` | 8 | 是 | - |
| 5 | `lastdate` | 推送日期 | `varchar2` | 1000 | 是 | - |
| 6 | `lasttime` | 推送时间 | `varchar2` | 1000 | 是 | - |
| 7 | `status` | 补丁包升级状态内容 | `varchar2` | 8 | 是 | 0：未升级 1：已升级 |
| 8 | `content` | 补丁包内容 | `varchar2` | 4000 | 是 | - |
| 9 | `downloadid` | 补丁包下载id | `varchar2` | 800 | 是 | - |
| 10 | `description` | 补丁包说明 | `varchar2` | 4000 | 是 | - |
