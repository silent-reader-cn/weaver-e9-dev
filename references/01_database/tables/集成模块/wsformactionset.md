# 泛微OA 数据表: `wsformactionset`

- **所属模块**: `集成模块`
- **数据库表名**: `wsformactionset`
- **字段总数**: `21`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `createdate` | 创建日期 | `varchar2` | 80 | 是 | 无 |
| 2 | `createtime` | 创建时间 | `varchar2` | 64 | 是 | 无 |
| 3 | `modifydate` | 修改日期 | `varchar2` | 80 | 是 | 无 |
| 4 | `modifytime` | 修改时间 | `varchar2` | 64 | 是 | 无 |
| 5 | `id` | 主键 | `integer` | - | 否 | 无 |
| 6 | `actionname` | 接口名称 | `varchar2` | 1000 | 是 | 无 |
| 7 | `formid` | 表单id | `integer` | - | 是 | 无 |
| 8 | `isbill` | 是否单据 | `integer` | - | 是 | 无 |
| 9 | `inpara` | 输入参数 | `varchar2` | 1000 | 是 | 无 |
| 10 | `actionorder` | 序号 | `integer` | - | 是 | 无 |
| 11 | `wsurl` | webservice地址 | `varchar2` | 1000 | 是 | 无 |
| 12 | `wsoperation` | webservice方法 | `varchar2` | 800 | 是 | 无 |
| 13 | `xmltext` | xml格式 | `long` | 0 | 是 | 无 |
| 14 | `rettype` | 返回值类型 | `integer` | - | 是 | 无 |
| 15 | `retstr` | 返回值字符串 | `varchar2` | 2000 | 是 | 无 |
| 16 | `webservicefrom` | 未知字段 | `varchar2` | 1000 | 是 | 无 |
| 17 | `custominterface` | 自定义接口 | `varchar2` | 1000 | 是 | 无 |
| 18 | `typename` | 接口类型 | `char` | 1 | 是 | 无 |
| 19 | `oldwsactionsetid` | 未知字段 | `integer` | - | 是 | 无 |
| 20 | `oldtype` | 未知字段 | `integer` | - | 是 | 无 |
| 21 | `wsnamespace` | webservice命名空间 | `varchar2` | 1000 | 是 | 无 |
