package com.custom.schedule;

import weaver.conn.RecordSet;
import weaver.general.BaseBean;
import weaver.interfaces.schedule.BaseCronJob;

/**
 * 泛微 Ecology 9 自定义计划任务 (CronJob)
 * 应用场景：每天定时从中间库或外部系统同步业务数据
 */
public class CustomCronJob extends BaseCronJob {

    private final BaseBean log = new BaseBean();

    @Override
    public void execute() {
        log.writeLog("===> [CustomCronJob] 定时任务启动执行...");
        long startTime = System.currentTimeMillis();

        try {
            // 1. 查询待处理记录
            RecordSet rs = new RecordSet();
            String querySql = "SELECT id, sync_type, payload FROM uf_sync_queue WHERE sync_status = 0 ORDER BY id ASC";
            rs.executeQuery(querySql);

            int processedCount = 0;
            RecordSet updateRs = new RecordSet();

            while (rs.next()) {
                String id = rs.getString("id");
                String syncType = rs.getString("sync_type");
                String payload = rs.getString("payload");

                log.writeLog("处理同步队列 ID=" + id + ", 类型=" + syncType);

                // 2. 模拟业务处理
                boolean ok = processItem(syncType, payload);

                // 3. 更新同步状态
                if (ok) {
                    updateRs.executeUpdate("UPDATE uf_sync_queue SET sync_status = 1, sync_time = ? WHERE id = ?",
                            weaver.general.TimeUtil.getCurrentTimeString(), id);
                } else {
                    updateRs.executeUpdate("UPDATE uf_sync_queue SET sync_status = 2, error_msg = '处理异常' WHERE id = ?", id);
                }
                processedCount++;
            }

            long cost = System.currentTimeMillis() - startTime;
            log.writeLog("===> [CustomCronJob] 执行完成! 共处理: " + processedCount + " 条记录, 耗时: " + cost + "ms");

        } catch (Exception e) {
            log.writeLog("===> [CustomCronJob] 执行异常: " + e.getMessage());
        }
    }

    private boolean processItem(String syncType, String payload) {
        // 实际业务逻辑实现
        return true;
    }
}
