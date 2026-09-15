# 泛微OA 数据表: `hrmsalarycalrate`

- **所属模块**: `人力资源`
- **数据库表名**: `hrmsalarycalrate`
- **字段总数**: `7`

## 表结构定义 (Schema)

| 序号 | 列名 (Column) | 中文说明 | 数据类型 | 长度 | 允许为空 | 字段备注 |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 1 | `id` | ID | `integer` | - | 否 | - |
| 2 | `benchid` | 公式id | `integer` | - | 是 | - |
| 3 | `timescope` | 时间范围 | `integer` | - | 是 | 年度 、半年度 、 季度 、月度 |
| 4 | `condition` | 条件 | `varchar2` | 1000 | 是 | - |
| 5 | `formular` | 计算规则 | `varchar2` | 1000 | 是 | - |
| 6 | `conditiondsp` | 条件描述 | `varchar2` | 1000 | 是 | - |
| 7 | `formulardsp` | 详情描述 | `varchar2` | 1000 | 是 | - |
