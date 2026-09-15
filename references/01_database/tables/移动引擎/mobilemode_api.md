# 泛微OA 数据表: `mobilemode_api`

- **所属模块**: `移动引擎`
- **数据库表名**: `mobilemode_api`
- **字段总数**: `20`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `type` | 类型 | `varchar2` | 400 | 是 | - |
| 2 | `is_sys` | 是否系统接口 | `varchar2` | 160 | 是 | 1为是，0为否 |
| 3 | `front_request_body_enabled` | 启用请求Body | `varchar2` | 400 | 是 | - |
| 4 | `front_request_body_desc` | 请求Body内容示例 | `varchar2` | 2000 | 是 | - |
| 5 | `id` | 主键 | `varchar2` | 32 | 否 | - |
| 6 | `groupid` | 分组Id | `varchar2` | 256 | 是 | 分组Id |
| 7 | `name` | 名称 | `varchar2` | 1000 | 是 | 名称 |
| 8 | `remark` | 备注 | `varchar2` | 2000 | 是 | 备注 |
| 9 | `front_path` | 前端路径 | `varchar2` | 200 | 是 | 前端路径 |
| 10 | `front_request_method` | 前端请求方法 | `varchar2` | 400 | 是 | POST |
| 11 | `server_addr` | 后端地址 | `varchar2` | 1000 | 是 | 后端地址 |
| 12 | `server_path` | 后端请求路径 | `varchar2` | 1000 | 是 | 后端请求路径 |
| 13 | `server_request_method` | 后端请求方法 | `varchar2` | 400 | 是 | 后端请求方法 |
| 14 | `server_timeout` | 超时时间 | `integer` | - | 是 | 单位：秒 |
| 15 | `return_contenttype` | 返回内容类型 | `varchar2` | 400 | 是 | - |
| 16 | `return_result_example` | 返回结果示例 | `varchar2` | 4000 | 是 | - |
| 17 | `creator` | 创建人 | `integer` | - | 是 | - |
| 18 | `create_time` | 创建时间 | `varchar2` | 160 | 是 | - |
| 19 | `modifier` | 修改人 | `integer` | - | 是 | - |
| 20 | `modify_time` | 修改时间 | `varchar2` | 160 | 是 | - |
