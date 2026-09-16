# 泛微OA 数据表: `esb_const`

- **中文名称**: ESB常量表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_const`
- **主键**: `constcode`
- **字段数**: `9`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `constcode` | 常量标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 2 | `constname` | 常量名称 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 3 | `productcode` | 产品标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 4 | `consttype` | 常量类别 | `varchar2` | 800 | 否 | 否 | 否 | - | - | string、int、double、date、datetime、password |
| 5 | `constvalue` | 常量值 | `varchar2` | 800 | 否 | 否 | 否 | - | - | - |
| 6 | `CREATEDATE` | 创建日期 | `varchar2` | 80 | 否 | 否 | 否 | - | - | - |
| 7 | `CREATETIME` | 创建时间 | `varchar2` | 80 | 否 | 否 | 否 | - | - | - |
| 8 | `MODIFYDATE` | 修改日期 | `varchar2` | 80 | 否 | 否 | 否 | - | - | - |
| 9 | `MODIFYTIME` | 修改时间 | `varchar2` | 80 | 否 | 否 | 否 | - | - | - |
