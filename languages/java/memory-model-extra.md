#### 原子性
- 为了保证原子性，提供了两个高级的字节码指令 Monitorenter 和 Monitorexit

#### 可见性
- Java 内存模型是通过在变量修改后将新值同步回主内存，在变量读取前从主内存刷新变量值的这种依赖主内存作为传递媒介的方式来实现的
- Java 中的 Volatile 关键字提供了一个功能，那就是被其修饰的变量在被修改后可以立即同步到主内存

#### 有序性
- 可以使用 Synchronized 和 Volatile 来保证多线程之间操作的有序性
- Volatile 关键字会禁止指令重排。Synchronized 关键字保证同一时刻只允许一条线程操作
