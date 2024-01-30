const std = @import("std");
const expect = std.testing.expect;

pub fn main() !void {
    var n: [100]u8 = undefined;
    var a: [100]u8 = undefined;
    var b: [100]u8 = undefined;
    var c: [100]u8 = undefined;
    const stdin = std.io.getStdIn().reader();
    const stdout = std.io.getStdOut().writer();

    _ = try stdin.readUntilDelimiter(&n, '\n');
    _ = try stdin.readUntilDelimiter(&a, '\n');
    _ = try stdin.readUntilDelimiter(&b, '\n');
    _ = try stdin.readUntilDelimiter(&c, '\n');

    try stdout.print("The user entered: {s}\n", .{n});
    try stdout.print("The user entered: {s}\n", .{a});
    try stdout.print("The user entered: {s}\n", .{b});
    try stdout.print("The user entered: {s}\n", .{c});
}

pub fn coins(n: i64, a: i64, b: i64, c: i64) i64 {
    if (n < 0) return @as(i64, @bitCast(std.math.inf(f64)));
    if (n == 0) return 0;
    return min(n, 1 + coins(n - a, a,b,c), 1 + coins(n - b, a,b,c), 1 + coins(n - c, a,b,c));
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

test "coin change 3" {
    const tmp = coins(0, 10, 100, 1000);
    try expect(tmp == 0);
}
