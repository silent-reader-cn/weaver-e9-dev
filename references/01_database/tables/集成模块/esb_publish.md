# 泛微OA 数据表: `esb_publish`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_publish`
- **字段总数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `publishid` | 发布服务标识 | `varchar2` | 100 | 否 | - |
| 2 | `publishname` | 发布服务名称 | `varchar2` | 800 | 是 | - |
| 3 | `publishtype` | 发布服务类型 | `varchar2` | 800 | 是 | 1:启用，0:未启用 |
| 4 | `state` | 状态 | `char` | 1 | 是 | - |
| 5 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | - |
| 6 | `createtime` | 创建时间 | `varchar2` | 80 | 是 | - |
| 7 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | - |
| 8 | `modifytime` | 修改时间 | `varchar2` | 80 | 是 | - |
| 9 | `version` | 版本号 | `integer` | - | 是 | - |
