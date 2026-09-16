# 泛微OA 数据表: `hrm_compensationtargetdetail`

- **中文名称**: 薪酬指标数据维护信息表
- **所属模块**: `人力资源`
- **数据库表名**: `hrm_compensationtargetdetail`
- **主键**: `id`
- **字段数**: `3`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文名称 | 数据类型 | 长度 | 允许为空 | 是否为外键 | 是否自增长 | 外键信息 | 默认值 | 说明 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `compensationtargetid` | 指标数据id | `integer` | - | 是 | 否 | 否 | - | - | 指标数据id |
| 2 | `targetid` | 指标id | `integer` | - | 是 | 否 | 否 | - | - | 指标id |
| 3 | `target` | 指标值 | `number` | (15,2) | 是 | 否 | 否 | - | - | 指标值 |
