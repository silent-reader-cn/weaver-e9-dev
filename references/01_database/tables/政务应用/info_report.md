# 泛微OA 数据表: `info_report`

- **所属模块**: `政务应用`
- **数据库表名**: `info_report`
- **字段总数**: `14`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | 数据id | `integer` | - | 否 | - |
| 2 | `uuid` | 32位随机id | `varchar2` | 32 | 是 | 用于做主键返回 |
| 3 | `pathid` | 路径id | `integer` | - | 是 | info_path表主键id |
| 4 | `title` | 标题 | `varchar2` | 256 | 是 | - |
| 5 | `reportType` | 报送类型 | `integer` | - | 是 | 0正常  1专报 |
| 6 | `reporter` | 上报人 | `integer` | - | 是 | - |
| 7 | `reportorg` | 报送单位 | `integer` | - | 是 | - |
| 8 | `reportdate` | 报送日期 | `varchar2` | 10 | 是 | - |
| 9 | `reporttime` | 报送时间 | `varchar2` | 8 | 是 | - |
| 10 | `source` | 信息来源 | `varchar2` | 256 | 是 | - |
| 11 | `content` | 正文 | `clob` | - | 是 | - |
| 12 | `atach` | 附件 | `clob` | - | 是 | - |
| 13 | `status` | 状态 | `integer` | - | 是 | 0待报、1审批中、2驳回、3审批通过、4已采用、5已发布 |
| 14 | `siftStatus` | 采编状态 | `integer` | - | 是 | 0已筛选、1未签收、2已签收、3驳回、4已采用、5特殊采用、6专报采用、7已发布 |
