package edu.umd.enpm614.assignment2;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.springframework.stereotype.Component;
import org.aspectj.lang.annotation.Aspect;

public class LogginAspect {
	@Component
	@Aspect
    //FrontendGWT
    @Around("within(edu.umd.enpm614.assignment2.services.*) && execution(public * *edu.umd.enpm614.assignment2.services.FrontendGWT.*(..))")
    public Object logExecutionTimeFrontGWT(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Loging Aspect: ");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName " + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName " + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime)
                .append(" ns");
        System.out.println(sb.toString());
        return value;
    }
    //FrontendHTML
    @Around("within(edu.umd.enpm614.assignment2.services.*) && execution(public * *edu.umd.enpm614.assignment2.services.FrontendHTML.*(..))"
    ) public Object logExecutionTimeFrontHTML(ProceedingJoinPoint joinPoint)
            throws Throwable { StringBuilder sb = new StringBuilder("Loging Aspect: ");
        long startTime = System.nanoTime(); Object value = joinPoint.proceed();
        sb.append(" QualifiedClassName " +
                        joinPoint.getSignature().getDeclaringTypeName()) .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime) .append(" ns");
        System.out.println(sb.toString()); return value; }
    //MiddlewareJBoss
    @Around("within(edu.umd.enpm614.assignment2.services.*) && execution(public * *edu.umd.enpm614.assignment2.services.MiddlewareJBoss.*(..))"
    ) public Object logExecutionTimeMiddleJBoss(ProceedingJoinPoint joinPoint)
            throws Throwable { StringBuilder sb = new StringBuilder("Loging Aspect: ");
        long startTime = System.nanoTime(); Object value = joinPoint.proceed();
        sb.append(" QualifiedClassName " +
                        joinPoint.getSignature().getDeclaringTypeName()) .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime) .append(" ns");
        System.out.println(sb.toString()); return value; }
    //MiddlewareJBoss
    @Around("within(edu.umd.enpm614.assignment2.services.*) && execution(public * *edu.umd.enpm614.assignment2.services.MiddlewareTomcat.*(..))"
    ) public Object logExecutionTimeMiddleTomcat(ProceedingJoinPoint joinPoint)
            throws Throwable { StringBuilder sb = new StringBuilder("Loging Aspect: ");
        long startTime = System.nanoTime(); Object value = joinPoint.proceed();
        sb.append(" QualifiedClassName " +
                        joinPoint.getSignature().getDeclaringTypeName()) .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime) .append(" ns");
        System.out.println(sb.toString()); return value; }
    //PersistanceMySQL
    @Around("within(edu.umd.enpm614.assignment2.services.*) && execution(public * *edu.umd.enpm614.assignment2.services.PersistanceMySQL.*(..))"
    ) public Object logExecutionTimePersistanceMySQL(ProceedingJoinPoint
                                                             joinPoint) throws Throwable { StringBuilder sb = new
            StringBuilder("Loging Aspect: "); long startTime = System.nanoTime(); Object
            value = joinPoint.proceed(); sb.append("QualifiedClassName " +
                    joinPoint.getSignature().getDeclaringTypeName()) .append(".")
            .append("methodName" + joinPoint.getSignature().getName())
            .append(" is ").append(System.nanoTime() - startTime) .append(" ns");
        System.out.println(sb.toString()); return value; }
    //PersistanceOracle
    @Around("within(edu.umd.enpm614.assignment2.services.*) && execution(public* *edu.umd.enpm614.assignment2.services.PersistanceOracle.*(..))"
    ) public Object logExecutionTimePersistanceOracle(ProceedingJoinPoint
                                                              joinPoint) throws Throwable { StringBuilder sb = new
            StringBuilder("Loging Aspect: "); long startTime = System.nanoTime(); Object
            value = joinPoint.proceed(); sb.append("QualifiedClassName " +
                    joinPoint.getSignature().getDeclaringTypeName()) .append(".")
            .append("methodName" + joinPoint.getSignature().getName())
            .append(" is ").append(System.nanoTime() - startTime) .append(" ns");
        System.out.println(sb.toString()); return value; }
    //AuthenticationSSL

    @Around("within(edu.umd.enpm614.assignment2.services.) && execution(public edu.umd.enpm614.assignment2.services.AuthenticationSSL.(..))")
    public Object logExecutionTimeAuthenticationSSL(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Logging Aspect:");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName" + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime).append("ms");
        System.out.println(sb.toString());
        return value;
    }
    //AuthenticationTSL
    @Around("within(edu.umd.enpm614.assignment2.services.) && execution(public edu.umd.enpm614.assignment2.services.AuthenticationTSL.(..))")
    public Object logExecutionTimeAuthenticationTSL(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Logging Aspect:");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName" + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime).append("ms");
        System.out.println(sb.toString());
        return value;
    }
    //FileSystemNTFS
    @Around("within(edu.umd.enpm614.assignment2.services.) && execution(public edu.umd.enpm614.assignment2.services.FileSystemNTFS.(..))")
    public Object logExecutionTimeFileSystemNTFS(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Logging Aspect:");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName" + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime).append("ms");
        System.out.println(sb.toString());
        return value;
    }
    //FileSystemNFS
    @Around("within(edu.umd.enpm614.assignment2.services.) && execution(public edu.umd.enpm614.assignment2.services.FileSystemNFS.(..))")
    public Object logExecutionTimeFileSystemNFS(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Logging Aspect:");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName" + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime).append("ms");
        System.out.println(sb.toString());
        return value;
    }
    //ConnectionPooled
    @Around("within(edu.umd.enpm614.assignment2.services.) && execution(public edu.umd.enpm614.assignment2.services.ConnectionPooled.(..))")
    public Object logExecutionTimeFileConnectionPooled(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Logging Aspect:");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName" + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime).append("ms");
        System.out.println(sb.toString());
        return value;
    }
    //ConnectionJDBC
    @Around("within(edu.umd.enpm614.assignment2.services.) && execution(public edu.umd.enpm614.assignment2.services.ConnectionJDBC.(..))")
    public Object logExecutionTimeFileConnectionJDBC(ProceedingJoinPoint joinPoint) throws Throwable {
        StringBuilder sb = new StringBuilder("Logging Aspect:");
        long startTime = System.nanoTime();
        Object value = joinPoint.proceed();
        sb.append("QualifiedClassName" + joinPoint.getSignature().getDeclaringTypeName())
                .append(".")
                .append("methodName" + joinPoint.getSignature().getName())
                .append(" is ").append(System.nanoTime() - startTime).append("ms");
        System.out.println(sb.toString());
        return value;
    }

}
