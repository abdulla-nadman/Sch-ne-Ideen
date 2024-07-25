class Vector {
    constructor(x, y) {
        this.x = x || 0;
        this.y = y || 0;
    }
    static sub(v1, v2) {
        return new Vector(v1.x - v2.x, v1.y - v2.y);
    }
    add(x, y) {
        if (arguments.length === 1) {
            this.x += x.x;
            this.y += x.y;
        } else if (arguments.length === 2) {
            this.x += x;
            this.y += y;
        }
        return this;
    }
    setXY(x, y) {
        this.x = x;
        this.y = y;
        return this;
    }
    dist(v) {
        const dx = this.x - v.x;
        const dy = this.y - v.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
    mult(scalar) {
        this.x *= scalar;
        this.y *= scalar;
        return this;
    }
  }
class Dot {
    constructor(x, y) {
        this.pos = new Vector(x, y);
        this.oldPos = new Vector(x, y);
        this.friction = 0.97;
        this.gravity = new Vector(0, 0.6);
        this.mass = 10; // Grî·eren Wert fÅr bessere Sichtbarkeit
        this.pinned = false;
        this.origin = origin; // Ursprung des Fadens
        this.ropeLength = 100; // LÑnge des Fadens
    }
}