import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = dirname(fileURLToPath(import.meta.url));
const enginePath = join(dir, '../shared/mock-cart-engine.js');
const src = readFileSync(enginePath, 'utf8');
const fn = new Function('globalThis', src + '\nreturn globalThis.BarreleticsMockCart;');
const M = fn(globalThis);

let s = M.initialState();
assert.equal(M.pairCount(s), 1);
assert.ok(M.availableColors(s, 'closed').includes('Purple'));

s.pick = { sole: 'closed', color: 'Purple', size: 'M (W 5.5-7.5)' };
s = M.addPair(s);
assert.equal(M.pairCount(s), 2);
assert.equal(M.stage(s), 'pants-offer');

s = M.removeLastPair(s);
assert.equal(M.pairCount(s), 1);

s.pick = { sole: 'open', color: 'Black', size: 'L (W 8-11)' };
s = M.addPair(s);
assert.equal(M.pairCount(s), 2);

console.log('mock-engine.test.mjs: pass (same + different color add)');
