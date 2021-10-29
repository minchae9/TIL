/*
	[배열 관련 주요 메서드 연습 1]
	
	주어진 배열의 요소 중 null 값을 제거한 새로운 배열을 만드세요.
*/

const homeworks = ['david.zip', null, 'maria.zip', 'tom.zip', null]


let ans = []
for (let homework of homeworks) {
	if (homework != null) {
		ans.push(homework)
	}
}
console.log(ans)


// 풀이
const results = []
for (const homework of homeworks) {
	if (homework) {
		results.push(homework)
	}
}
console.log(results)

/*
	[배열 관련 주요 메서드 연습 2]
	
	주어진 배열을 사용하여 아래 문자열을 완성하세요.

	'www.samsung.com/sec/buds/galaxy-buds-pro'

*/

const arr1 = ['www', 'samsung', 'com']
const arr2 = ['galaxy', 'buds', 'pro']
const arr3 = ['sec', 'buds']

// 1)
let result
result = arr1.join('.') + '/' + arr3.join('/') + '/' +  arr2.join('-')
console.log(result)
// 2)
let ans = []
ans.push(arr1.join('.'))
ans.push(arr3.join('/')) 
ans.push(arr2.join('-'))
console.log(ans.join('/'))


// 풀이
const homepage = arr1.join('.')		// www.samsung.com
const product = arr2.join('-')		// galaxy-buds-pro
arr3.unshift(homepage)						// ['www.samsung.com', 'sec', 'buds']
arr3.push(product)								// ['www.samsung.com', 'sec', 'buds', 'galaxy-buds-pro']
const result = arr3.join('/')
console.log(result)								// www.samsung.com/sec/buds/galaxy-buds-pro




/*
	[배열 관련 주요 메서드 연습 3]

	주어진 배열의 요소 중 모든 'rainy' 요소를 'sunny'로 교체하세요
	- indexOf 메서드를 사용합니다.
*/

const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']

while (weather.indexOf('rainy') > -1) {
	weather[weather.indexOf('rainy')] = 'sunny'
}
console.log(weather)

// 풀이
while (weather.indexOf('rainy') >= 0) {				// 없으면 indexOf의 반환값이 -1 이므로
	weather[weather.indexOf('rainy')] = 'sunny'
}
console.log(weather)