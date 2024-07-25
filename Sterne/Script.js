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
    constructor(x, y, origin) {
        this.pos = new Vector(x, y);
        this.oldPos = new Vector(x, y);
        this.friction = 0.97;
        this.gravity = new Vector(0, 0.6);
        this.mass = 10;
        this.pinned = false;
        this.origin = origin;
        this.ropeLength = 100;
    }
  
    update(mouse) {
        if (this.pinned) return;
  
        let vel = Vector.sub(this.pos, this.oldPos);
        this.oldPos.setXY(this.pos.x, this.pos.y);
  
        vel.mult(this.friction);
        vel.add(this.gravity);
  
        let { x: dx, y: dy } = Vector.sub(mouse.pos, this.pos);
        const dist = Math.sqrt(dx * dx + dy * dy);
        const direction = new Vector(dx / dist, dy / dist);
        const force = Math.max((mouse.radius - dist) / mouse.radius, 0);
  
        if (force > 0.6) this.pos.setXY(mouse.pos.x, mouse.pos.y);
        else {
            this.pos.add(vel);
            this.pos.add(direction.mult(force));
        }
  
        let ropeDist = Vector.sub(this.pos, this.origin);
        let ropeLength = ropeDist.dist(new Vector(0, 0));
        if (ropeLength > this.ropeLength) {
            ropeDist = ropeDist.mult(1 - this.ropeLength / ropeLength);
            this.pos.setXY(this.origin.x + ropeDist.x, this.origin.y + ropeDist.y);
        }
  
        // Restoring force to bring the dot back to its origin
        let originDist = Vector.sub(this.origin, this.pos);
        this.pos.add(originDist.mult(0.05)); // Adjust the restoring speed as needed
    }
  
    draw(ctx) {
        ctx.beginPath();
        ctx.moveTo(this.origin.x, this.origin.y);
        ctx.lineTo(this.pos.x, this.pos.y);
        ctx.strokeStyle = '#aaa';
        ctx.stroke();
  
        ctx.fillStyle = '#aaa';
        ctx.fillRect(this.pos.x - this.mass / 2, this.pos.y - this.mass / 2, this.mass, this.mass);
    }
  }
  
  class Mouse {
    constructor(canvas) {
        this.pos = new Vector(-1000, -1000);
        this.radius = 40;
        canvas.onmousemove = e => this.pos.setXY(e.clientX, e.clientY);
        canvas.ontouchmove = e => this.pos.setXY(e.touches[0].clientX, e.touches[0].clientY);
        canvas.ontouchcancel = () => this.pos.setXY(-1000, -1000);
        canvas.ontouchend = () => this.pos.setXY(-1000, -1000);
    }
  }
  
  class App {
    static width = innerWidth;
    static height = innerHeight;
    static dpr = devicePixelRatio > 1 ? 2 : 1;
    static interval = 1000 / 60;
  
    constructor() {
        this.canvas = document.querySelector('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.mouse = new Mouse(this.canvas);
        this.resize();
        window.addEventListener('resize', this.resize.bind(this));
        this.createDots();
        this.render();
    }
  
    createDots() {
        this.dots = [];
        const centerX = App.width / 2;
        const centerY = App.height / 2;
        for (let i = 0; i < 10; i++) {
            this.dots.push(new Dot(centerX + i * 20, centerY, new Vector(centerX + i * 20, centerY - 100)));
        }
    }
  
    resize() {
        App.width = innerWidth;
        App.height = innerHeight;
        this.canvas.style.width = '100%';
        this.canvas.style.height = '100%';
        this.canvas.width = App.width * App.dpr;
        this.canvas.height = App.height * App.dpr;
        this.ctx.scale(App.dpr, App.dpr);
    }
  
    render() {
        let now, delta;
        let then = Date.now();
        const frame = () => {
            requestAnimationFrame(frame);
            now = Date.now();
            delta = now - then;
            if (delta < App.interval) return;
            then = now - (delta % App.interval);
            this.ctx.clearRect(0, 0, App.width, App.height);
            this.dots.forEach(dot => {
                dot.update(this.mouse);
                dot.draw(this.ctx);
            });
        };
        requestAnimationFrame(frame);
    }
  }
  
  window.addEventListener('load', () => {
    new App();
  });
  