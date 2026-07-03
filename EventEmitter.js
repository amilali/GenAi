class EventEmitter {
  constructor() {
    this.events = {};
  }

  /**
   * Register an event listener for a given event.
   * @param {string} event - The name of the event.
   * @param {Function} listener - The callback function to execute when event is emitted.
   * @returns {EventEmitter} - Returns `this` for chaining.
   */
  on(event, listener) {
    if (typeof listener !== 'function') {
      throw new TypeError('Listener must be a function');
    }
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(listener);
    return this;
  }

  /**
   * Remove a specific event listener for a given event.
   * @param {string} event - The name of the event.
   * @param {Function} listener - The callback function to remove.
   * @returns {EventEmitter} - Returns `this` for chaining.
   */
  off(event, listener) {
    if (!this.events[event]) {
      return this;
    }
    this.events[event] = this.events[event].filter(
      (l) => l !== listener && l.originalListener !== listener
    );
    return this;
  }

  /**
   * Trigger/emit an event, executing all registered listeners with the provided arguments.
   * @param {string} event - The name of the event to emit.
   * @param {...any} args - Arguments to pass to the listener callbacks.
   * @returns {boolean} - Returns true if the event has listeners, false otherwise.
   */
  emit(event, ...args) {
    if (!this.events[event] || this.events[event].length === 0) {
      return false;
    }
    // Clone the array to avoid bugs if listeners are added or removed during emission
    const listeners = [...this.events[event]];
    listeners.forEach((listener) => {
      listener.apply(this, args);
    });
    return true;
  }

  /**
   * Register a one-time event listener. It will be removed automatically after the first invocation.
   * @param {string} event - The name of the event.
   * @param {Function} listener - The callback function to execute.
   * @returns {EventEmitter} - Returns `this` for chaining.
   */
  once(event, listener) {
    if (typeof listener !== 'function') {
      throw new TypeError('Listener must be a function');
    }
    const wrapper = (...args) => {
      this.off(event, wrapper);
      listener.apply(this, args);
    };
    // Keep reference to original listener so .off() can find and remove it before it triggers
    wrapper.originalListener = listener;
    this.on(event, wrapper);
    return this;
  }

  /**
   * Remove all listeners, or those of a specified event.
   * @param {string} [event] - Optional name of the event. If omitted, all events are cleared.
   * @returns {EventEmitter} - Returns `this` for chaining.
   */
  removeAllListeners(event) {
    if (event) {
      delete this.events[event];
    } else {
      this.events = {};
    }
    return this;
  }
}

// Export for common module systems (Node.js / ES Modules fallback)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = EventEmitter;
}


// Example Usage (only runs if executed directly)
if (typeof require !== 'undefined' && require.main === module) {
  const emitter = new EventEmitter();

  // Test .on()
  emitter.on('greet', (name) => {
    console.log(`Hello, ${name}!`);
  });

  // Test .once()
  emitter.once('single-time', () => {
    console.log('This will only print once.');
  });

  console.log('--- Emitting greet ---');
  emitter.emit('greet', 'Alice');

  console.log('--- Emitting single-time twice ---');
  emitter.emit('single-time');
  emitter.emit('single-time'); // Should not print
}



// ----------------------------------------------------------------------------------- //


const EventEmitter = require('./EventEmitter');

class ChatRoom extends EventEmitter {
  constructor(roomName) {
    super();
    this.roomName = roomName;
  }

  // When a user joins
  join(user) {
    console.log(`${user} joined ${this.roomName}`);
    this.emit('userJoined', user);
  }

  // When a message is sent
  sendMessage(user, message) {
    this.emit('message', { user, message, timestamp: new Date() });
  }
}

// --- Usage ---
const lobby = new ChatRoom('Lobby');

// 1. Logger component listens to all messages
lobby.on('message', ({ user, message, timestamp }) => {
  console.log(`[LOG] [${timestamp.toLocaleTimeString()}] ${user}: ${message}`);
});

// 2. Notification component listens to users joining
lobby.on('userJoined', (user) => {
  console.log(`[NOTIFICATION] Welcome ${user} to the chat!`);
});

// Simulate events happening
lobby.join('Alice');
lobby.sendMessage('Alice', 'Hello everyone!');
