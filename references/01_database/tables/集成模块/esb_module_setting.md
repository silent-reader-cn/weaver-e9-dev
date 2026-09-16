# 泛微OA 数据表: `esb_module_setting`

- **中文名称**: ESB模块设置维护表
- **所属模块**: `集成模块`
- **数据库表名**: `esb_module_setting`
- **主键**: `MODULECODE`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `MODULECODE` | 模块标识 | `varchar2` | 800 | 否 | 否 | 否 | - | - | 模块标识 |
| 2 | `MODULENAME` | 模块名称 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 模块名称 |
| 3 | `SUPMODULECODE` | 上级模块 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 上级模块 |
| 4 | `DESCRIPTION` | 描述 | `varchar2` | 2000 | 是 | 否 | 否 | - | - | 描述 |
| 5 | `SHOWSORT` | 显示顺序 | `integer` | - | 是 | 否 | 否 | - | - | 显示顺序 |
| 6 | `MODULELEVEL` | 模块菜单级别 | `integer` | - | 是 | 否 | 否 | - | - | 模块菜单级别 |
| 7 | `PRODUCTCODE` | 所属产品 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 所属产品 |
| 8 | `CREATEDATE` | 创建日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 创建日期 |
| 9 | `CREATETIME` | 创建时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 创建时间 |
| 10 | `MODIFYDATE` | 修改日期 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 修改日期 |
| 11 | `MODIFYTIME` | 修改时间 | `varchar2` | 80 | 是 | 否 | 否 | - | - | 修改时间 |
