# 泛微OA 数据表: `esb_category`

- **所属模块**: `集成模块`
- **数据库表名**: `esb_category`
- **字段总数**: `10`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `CATEGORYID` | 类别标识 | `varchar2` | 800 | - | 类别标识 |
| 2 | `CATEGORYNAME` | 类别名称 | `varchar2` | 800 | - | 类别名称 |
| 3 | `SUPCATEGORYID` | 上级类别 | `varchar2` | 800 | - | 上级类别 |
| 4 | `DESCRIPTION` | 描述说明 | `clob` | - | - | 描述说明 |
| 5 | `SHOWSORT` | 显示顺序 | `integer` | 11 | - | 显示顺序 |
| 6 | `CATEGORYLEVEL` | 级别 | `integer` | 11 | - | 级别（暂时不用） |
| 7 | `CREATEDATE` | 创建日期 | `varchar2` | 800 | - | 创建日期 |
| 8 | `CREATETIME` | 创建时间 | `varchar2` | 800 | - | 创建时间 |
| 9 | `MODIFYDATE` | 修改日期 | `varchar2` | 800 | - | 修改日期 |
| 10 | `MODIFYTIME` | 修改时间 | `varchar2` | 800 | - | 修改时间 |
