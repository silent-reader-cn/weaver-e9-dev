# 泛微OA 数据表: `hrmsubcompany`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsubcompany`
- **字段总数**: `18`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `created` | 创建时间 | `timestamp(6)` | 11 | 是 | 创建时间 |
| 2 | `creater` | 创建人 | `integer` | - | 是 | 创建人 |
| 3 | `modified` | 修改时间 | `timestamp(6)` | 11 | 是 | 创建人 |
| 4 | `modifier` | 修改人 | `integer` | - | 是 | 创建人 |
| 5 | `id` | ID | `integer` | - | 否 | ID |
| 6 | `subcompanyname` | 分部简称 | `varchar2` | 1000 | 是 | 分部简称 |
| 7 | `subcompanydesc` | 分部描述 | `varchar2` | 1000 | 是 | 分部描述 |
| 8 | `companyid` | 所属总部id | `integer` | - | 是 | 所属总部id |
| 9 | `supsubcomid` | 上级分部id | `integer` | - | 是 | 上级分部id |
| 10 | `url` | 网址 | `varchar2` | 400 | 是 | 网址 |
| 11 | `showorder` | 序列号 | `integer` | - | 是 | 序列号 |
| 12 | `canceled` | 封存标识 | `char` | 1 | 是 | 封存标识 |
| 13 | `subcompanycode` | 分部编码 | `varchar2` | 800 | 是 | 分部编码 |
| 14 | `outkey` | 外键 | `varchar2` | 800 | 是 | 与其他系统集成同步时使用 |
| 15 | `budgetatuomoveorder` | 做预算结转时的临时排序用 | `integer` | - | 是 | 做预算结转时的临时排序用 |
| 16 | `ecology_pinyin_search` | 分部首字母拼音 | `varchar2` | 1000 | 是 | 分部首字母拼音 |
| 17 | `limitusers` | 限制用户数 | `integer` | - | 是 | 限制用户数 |
| 18 | `tlevel` | 等级 | `integer` | - | 是 | 等级 |
