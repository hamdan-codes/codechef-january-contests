// Contributor Chaudhary Hamdan
// 30 Points

#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while (t--)
	{	stack <long long int>stack ;
		long long int n, m;
		cin >> n >> m;
		long long int a[n], b[m];
		for (long long int i = 0; i < n; i++)
			cin >> a[i];
		for (long long int i = 0; i < m; i++)
			cin >> b[i];
		long long int x;
		unordered_set<long long int>s;
		stack.push(0);
		while (!stack.empty())
		{
			x = stack.top();
			stack.pop();
			for (long long int i = 0; i < n; i++)
			{
				long long int u = a[i];
				if (s.find(u | x) == s.end())
				{
					s.insert(u | x);
					stack.push(u | x);
				}
			}
			for (long long int i = 0; i < m; i++)
			{
				long long int u = b[i];
				if (s.find(u & x) == s.end())
				{
					s.insert(u & x);
					stack.push(u & x);
				}
			}
		}
		cout << s.size() << endl;


	}

	return 0;
}