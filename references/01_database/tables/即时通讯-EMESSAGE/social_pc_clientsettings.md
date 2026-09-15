# 泛微OA 数据表: `social_pc_clientsettings`

- **所属模块**: `即时通讯-EMESSAGE`
- **数据库表名**: `social_pc_clientsettings`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 主键id | `integer` | - | 否 | 主键id |
| 2 | `keytitle` | 配置项中文名 | `varchar2` | 800 | 否 | 配置项中文名 |
| 3 | `keyvalue` | 配置项值 | `varchar2` | 800 | 否 | 配置项值 |
| 4 | `oaidentity` | 暂时未知 | `varchar2` | 800 | 是 | 暂时未知 |
| 5 | `modifier` | 修改人 | `integer` | - | 是 | 修改人 |
| 6 | `modifydate` | 修改日期 | `char` | 10 | 是 | 修改日期 |
| 7 | `modifytime` | 修改时间 | `char` | 8 | 是 | 修改时间 |
| 8 | `fromtype` | 设置类型 | `char` | 1 | 否 | 0对应social/manager/SocialClientFunctionCommon.jsp;1对应/social/manager/SocialAppSettingCommon.jsp这个页面 |
| 9 | `labelid` | 不存在的字段 | `integer` | - | 是 | 不存在的字段 |
