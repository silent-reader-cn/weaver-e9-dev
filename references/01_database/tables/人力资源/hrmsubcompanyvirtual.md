# 泛微OA 数据表: `hrmsubcompanyvirtual`

- **中文名称**: 虚拟分部信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrmsubcompanyvirtual`
- **主键**: `id`
- **字段数**: `11`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | ID | `integer` | - | 否 | 否 | 否 | - | - | ID |
| 2 | `subcompanyname` | 分部名称 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 分部名称 |
| 3 | `subcompanycode` | 分部编码 | `varchar2` | 800 | 是 | 否 | 否 | - | - | 分部编码 |
| 4 | `subcompanydesc` | 分部描述 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 分部描述 |
| 5 | `supsubcomid` | 上级分部id | `integer` | - | 是 | 否 | 否 | - | 0 | 上级分部id |
| 6 | `companyid` | 公司id | `integer` | - | 是 | 否 | 否 | - | - | 公司id |
| 7 | `canceled` | 是否封存 | `char` | 1 | 是 | 否 | 否 | - | - | 0 解封，1封存 |
| 8 | `showorder` | 序列号 | `integer` | - | 是 | 否 | 否 | - | - | 序列号 |
| 9 | `tlevel` | 等级 | `integer` | - | 是 | 否 | 否 | - | - | 等级 |
| 10 | `virtualtypeid` | 虚拟类型id | `integer` | - | 是 | 否 | 否 | - | - | 虚拟类型id |
| 11 | `ecology_pinyin_search` | 拼音 | `varchar2` | 1000 | 是 | 否 | 否 | - | - | 拼音 |
