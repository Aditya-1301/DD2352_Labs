const std = @import("std");
const expect = std.testing.expect;

pub fn coins(n: i64, a: i64, b: i64, c: i64) i64 {
    if (n < 0) return -1;
    if (n == 0) return 0;
    return min(n, 1 + coins(n - a), 1 + coins(n - b), 1 + coins(n - c));
}

fn min(a: i64, b: i64, c: i64, d: i64) i64 {
    return @min(@min(a, b), @min(c, d));
}

test "checking min" {
    const tmp = min(50, 69, 420, 1337);
    try expect(tmp == 50);
}

test "checking min 2" {
    const tmp = min(-7, 15, -69, 1000);
    try expect(tmp == -69);
}

test "coin change 1" {
    const tmp = coins(10, 2, 3, 4);
    try expect(tmp == 3);
}

test "coin change 2" {
    const tmp = coins(10, 5, 6, 7);
    try expect(tmp == 2);
}

test "coin change output 3" {
    const tmp = coins(0, 10, 100, 1000);
    try expect(tmp == 0);
}
