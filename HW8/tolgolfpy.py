"""
fun main() {
	val I = 1 shl 30
	val (k, n, m, o) = L
	val g = n / k
	val s = Array(g * 2) { List(k) { Array(k) { I } } }
	repeat(m) {
		val (a, b, c) = L
		s[a / k + g][a % k][b % k] = c
	}
	fun List<Array<Int>>.m(b: List<Array<Int>>) = map {
		Array(k) { j ->
			minOf(it.zip(b) { x, y -> x + y[j] }.min()!!, I)
		}
	}
	for (i in g - 1 downTo 1) s[i] = s[i * 2].m(s[i * 2 + 1])
	val z = s[0]
	repeat(k) { z[it][it] = 0 }
	repeat(o) {
		var (a, b) = L
		a = a / k + g
		b = b / k + g
		var p = z
		var q = z
		while (a < b) {
			if (a % 2 == 1) p = p.m(s[a++])
			if (b % 2 == 1) q = s[--b].m(q)
			a /= 2
			b /= 2
		}
		val i = p.m(q)[a % k][b % k]
		println(if(i==I)-1 else i)
	}
}

val L get() = readLine()!!.split(" ").map { it.toInt() }

"""
# python golf version of toll
# L = lambda: map(int, input().split())
# k, n, m, o = L()
# g = n // k
# Z = range(k)
# s = [[[1e9] * k for _ in [0] * k] for _ in [0, 0] * g]
# for _ in [0] * m:
#     a, b, c = L()
#     s[a//k + g][a % k][b % k] = c
# m = lambda A, B: [[min(x + y[j] for x, y in zip(a, B)) for j in Z] for a in A]
# for i in range(g - 1, 0, -1): s[i] = m(s[i * 2], s[i * 2 + 1])
# z = s[0]
# for i in Z: z[i][i] = 0
# for _ in [0] * o:
#     a, b = L()
#     l,r,p,q = a // k + g, b // k + g, z, z
#     while l < r:
#         if l&1: p = m(p, s[l]); l += 1
#         if r&1: r -= 1; q = m(s[r], q)
#         l //= 2; r //= 2
#     print(-1 if (i := m(p, q)[a % k][b % k])>1e9 else i)

# now, extra minified
R=range
L=lambda:map(int,input().split())
k,n,m,o=L()
K=R(k)
s=[[k*[1e9]for _ in K]for _ in[0,0]*n]
for _ in[0]*m:a,b,c=L();s[a//k+n][a%k][b%k]=c
m=lambda A,B:[[min(a[k]+B[k][j]for k in K)for j in K]for a in A]
for i in R(n)[::-1]:s[i]=m(s[i*2],s[i*2+1])
for z in[s[0]]*o:
	for i in K:z[i][i]=0
	a,b=L();l,r,p,q=a//k+n,b//k+n,z,z
	while l<r:p=m(p,(z,s[l])[l&1]);q=m((z,s[~-r])[r%2],q);l=-~l//2;r>>=1
	print((~0,i:=m(p,q)[a%k][b%k])[i<1e9])
