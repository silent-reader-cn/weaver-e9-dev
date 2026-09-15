# 高频业务 SQL 模版

> 生产级 SQL 模版，直接可用。表结构定义见 [`tables/`](./tables/)。

## 1. 查询指定用户的当前待办流程列表 (带分页与未读状态)
```sql
SELECT 
    r.requestid,
    r.requestname,
    r.workflowid,
    w.workflowname,
    r.creater,
    u.lastname AS creater_name,
    r.createdate,
    r.createtime,
    c.receivedate,
    c.receivetime,
    c.viewtype -- 0:未读, 1:已读
FROM workflow_currentoperator c
INNER JOIN workflow_requestbase r ON c.requestid = r.requestid
INNER JOIN workflow_base w ON r.workflowid = w.id
LEFT JOIN HrmResource u ON r.creater = u.id
WHERE c.userid = 120 -- 替换为目标用户ID
  AND c.isremark IN ('0', '1', '8', '9', '7') -- 0:待办, 8:抄送待阅
  AND r.currentnodetype <> '3'
ORDER BY c.receivedate DESC, c.receivetime DESC;
```

## 2. 查询指定流程实例的所有流转签字意见 (审批历史全记录)
```sql
SELECT 
    l.logid,
    l.requestid,
    l.nodeid,
    n.nodename,
    l.operator,
    h.lastname AS operator_name,
    l.operatedate,
    l.operatetime,
    l.logtype,
    CASE l.logtype 
        WHEN 's' THEN '提交'
        WHEN 'r' THEN '退回'
        WHEN 'j' THEN '转办/征询'
        WHEN 'e' THEN '强制归档'
        WHEN 'i' THEN '干预'
        ELSE l.logtype 
    END AS action_name,
    l.remark AS sign_opinion -- 签字意见
FROM workflow_requestLog l
LEFT JOIN workflow_nodebase n ON l.nodeid = n.id
LEFT JOIN HrmResource h ON l.operator = h.id
WHERE l.requestid = 398210 -- 替换为流程 RequestID
ORDER BY l.operatedate ASC, l.operatetime ASC, l.logid ASC;
```

## 3. 递归查询某部门下的所有子部门 (CTE 通用表达式)
```sql
-- 支持 SQL Server 2008+ / MySQL 8.0+ / Oracle / PostgreSQL
WITH RECURSIVE DeptTree AS (
    SELECT id, departmentname, departmentcode, supdepid, subcompanyid1, 1 as level
    FROM HrmDepartment
    WHERE id = 5 -- 根部门ID
    
    UNION ALL
    
    SELECT d.id, d.departmentname, d.departmentcode, d.supdepid, d.subcompanyid1, t.level + 1
    FROM HrmDepartment d
    INNER JOIN DeptTree t ON d.supdepid = t.id
    WHERE d.canceled = '0'
)
SELECT * FROM DeptTree ORDER BY level, id;
```

## 4. 查询流程主表与明细表业务数据 (动态单据表)
```sql
-- 1. 先通过 workflowid 查找对应的单据主表名
SELECT b.id AS workflowid, b.workflowname, bill.tablename
FROM workflow_base b
INNER JOIN workflow_bill bill ON b.formid = bill.id
WHERE b.id = 105;

-- 2. 关联主表与明细表1查询业务数据
SELECT 
    m.requestid,
    m.sqr,          -- 申请人ID
    u.lastname AS sqr_name,
    m.sqje,         -- 申请金额
    d.wpmc,         -- 明细行物品名称
    d.sl,           -- 明细行数量
    d.dj,           -- 明细行单价
    d.je            -- 明细行金额
FROM formtable_main_105 m
INNER JOIN formtable_main_105_dt1 d ON m.id = d.mainid
LEFT JOIN HrmResource u ON m.sqr = u.id
WHERE m.requestid = 398210;
```
