# 泛微OA 数据表: `info_sifting`

- **中文名称**: 待编信息
- **所属模块**: `政务督办采编`
- **数据库表名**: `info_sifting`
- **主键**: `id`
- **字段数**: `27`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | 否 | 是 | - | - | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | 否 | 否 | - | - | 用于做主键返回 |
| 3 | `pathid` | 路径id | `integer` | - | 是 | 否 | 否 | - | - | info_path表主键id |
| 4 | `infoid` | 上报信息id | `varchar2` | 32 | 是 | 否 | 否 | - | - | info_report表主键id |
| 5 | `type` | 类型 | `integer` | - | 是 | 否 | 否 | - | - | 0正常 1专报 2特殊采用 |
| 6 | `title` | 标题 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 7 | `journal` | 所属期刊 | `integer` | - | 是 | 否 | 否 | - | - | info_journal表主键id |
| 8 | `score` | 总分 | `float` | - | 是 | 否 | 否 | - | - | - |
| 9 | `reporter` | 上报人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 10 | `reportorg` | 报送单位 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 11 | `reportdate` | 报送日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 12 | `reporttime` | 报送时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 13 | `source` | 信息来源 | `varchar2` | 256 | 是 | 否 | 否 | - | - | - |
| 14 | `content` | 正文 | `clob` | - | 是 | 否 | 否 | - | - | - |
| 15 | `atach` | 附件 | `clob` | - | 是 | 否 | 否 | - | - | - |
| 16 | `j_type` | 刊型 | `integer` | - | 是 | 否 | 否 | - | - | info_journaltype表主键id |
| 17 | `j_column` | 栏目 | `integer` | - | 是 | 否 | 否 | - | - | info_journalcolumn表主键id |
| 18 | `status` | 状态 | `integer` | - | 是 | 否 | 否 | - | - | 0已筛选、1已采用、2 已发布 |
| 19 | `filter` | 筛选人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 20 | `filterdate` | 筛选日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 21 | `filtertime` | 筛选时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 22 | `finalizer` | 定稿人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 23 | `finalizedate` | 定稿日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 24 | `finalizetime` | 定稿时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
| 25 | `releaser` | 发布人 | `integer` | - | 是 | 否 | 否 | - | - | - |
| 26 | `releasedate` | 发布日期 | `varchar2` | 10 | 是 | 否 | 否 | - | - | - |
| 27 | `releasetime` | 发布时间 | `varchar2` | 8 | 是 | 否 | 否 | - | - | - |
